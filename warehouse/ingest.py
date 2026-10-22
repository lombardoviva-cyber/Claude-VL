"""Unify Favikon exports in warehouse/raw/ into warehouse/posts.csv.

Each file is one account (file name = handle). Column names vary between
exports, so they are matched against the aliases below. Every post gets its
performance relative to the median of its own account.
"""
import sys
import unicodedata
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).parent
RAW = ROOT / "raw"
OUT = ROOT / "posts.csv"
WINNER_THRESHOLD = 2.0

ALIASES = {
    "url": ["url", "link", "post url", "post link", "permalink", "enlace"],
    "fecha": ["date", "published", "published at", "publication date", "posted at", "fecha"],
    "tipo": ["type", "format", "media type", "post type", "tipo", "formato"],
    "caption": ["caption", "text", "description", "content", "post text", "texto", "descripcion"],
    "vistas": ["views", "plays", "video views", "reach", "impressions", "vistas", "reproducciones"],
    "likes": ["likes", "like count", "me gusta"],
    "comentarios": ["comments", "comment count", "comentarios"],
    "compartidos": ["shares", "share count", "compartidos"],
    "guardados": ["saves", "save count", "saved", "guardados"],
    "duracion": ["duration", "video duration", "length", "duracion"],
    "transcripcion": ["transcript", "transcription", "on screen text", "transcripcion"],
}
METRICS = ["vistas", "likes", "comentarios", "compartidos", "guardados"]


def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode()
    return " ".join(s.lower().replace("_", " ").split())


def map_columns(df):
    lookup = {norm(c): c for c in df.columns}
    out = {}
    for field, names in ALIASES.items():
        for name in names:
            if name in lookup:
                out[field] = df[lookup[name]]
                break
    return pd.DataFrame(out)


def load(path):
    if path.suffix.lower() in (".xlsx", ".xls"):
        return pd.read_excel(path)
    return pd.read_csv(path)


def main():
    files = sorted(p for p in RAW.glob("*") if p.suffix.lower() in (".xlsx", ".xls", ".csv"))
    if not files:
        sys.exit(f"No hay archivos en {RAW}. Guardá ahí los exports de Favikon.")

    frames = []
    for path in files:
        df = map_columns(load(path))
        if df.empty:
            print(f"{path.name}: no reconocí ninguna columna, lo salteo")
            continue
        for m in METRICS:
            if m in df:
                df[m] = pd.to_numeric(df[m], errors="coerce")
        # Views when present, otherwise likes + comments.
        if "vistas" in df and df["vistas"].notna().any():
            df["metrica"] = df["vistas"]
            df["metrica_usada"] = "vistas"
        else:
            df["metrica"] = df.get("likes", 0).fillna(0) + df.get("comentarios", 0).fillna(0)
            df["metrica_usada"] = "likes+comentarios"
        median = df["metrica"].median()
        df["rendimiento_vs_mediana"] = (df["metrica"] / median).round(2) if median else None
        df["ganador"] = df["rendimiento_vs_mediana"] >= WINNER_THRESHOLD
        df["gancho"] = df.get("caption", pd.Series(dtype=str)).fillna("").astype(str).str.split("\n").str[0].str.slice(0, 200)
        df.insert(0, "cuenta", path.stem)
        for col in ["formato", "estructura", "serie", "gancho_plantilla", "adaptacion_vero"]:
            df[col] = ""
        frames.append(df)
        print(f"{path.name}: {len(df)} posts, mediana {median:,.0f} ({df['metrica_usada'].iat[0]}), {int(df['ganador'].sum())} ganadores")

    posts = pd.concat(frames, ignore_index=True).sort_values("rendimiento_vs_mediana", ascending=False)
    posts.to_csv(OUT, index=False)
    print(f"\n{len(posts)} posts en {OUT}")


if __name__ == "__main__":
    main()
