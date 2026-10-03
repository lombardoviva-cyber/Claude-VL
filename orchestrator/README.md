# Orquestador

Capa **03 · Orchestrator**. Todo pasa por acá; nada se publica sin tu aprobación.

```
Recolecta → Puntúa → Brief → Borrador → Aprobás → Programa
```

| Paso | Quién | Dónde queda |
|---|---|---|
| Recolecta | Routine `01-senales` | `marketing-os/research/trend-map.md` |
| Puntúa | Routine `01-senales` | Columna "Puntaje" de trend-map |
| Brief | Routine `02-borradores` | Planilla, estado "Brief" |
| Borrador | Routine `02-borradores` + skills | Planilla, estado "Borrador" |
| Aprobás | **Vero** | Planilla, estado "Aprobado" |
| Programa | Vero | Canva Pro (LinkedIn) · Buffer gratis (IG, TikTok, X) · Substack a mano |

## Control
- **Cola de aprobación:** filtro de la pestaña Calendario por estado = Borrador.
- **Log de actividad:** `orchestrator/activity-log.md` (cada Routine agrega una línea).
- **Botón de apagado:** desactivar las Routines desde claude.ai/code → Routines, o pedirle a Claude que las pause.

## Cómo activar las Routines
Pedile a Claude en una sesión de este repo: "activá las routines del orquestador".
Los prompts están en `orchestrator/routines/` (01 señales, 02 borradores, 03 reporte, 04 PR). Necesitan los conectores Google Drive y Windsor.ai.
