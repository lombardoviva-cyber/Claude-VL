# Orquestador

Capa **03 · Orchestrator**. Todo pasa por acá; nada se publica sin tu aprobación.

```
Recolecta → Puntúa → Brief → Borrador → Aprobás → Programa
```

| Paso | Quién | Dónde queda |
|---|---|---|
| Recolecta | Routine `01-senales` | `marketing-os/research/trend-map.md` |
| Puntúa | Routine `01-senales` | Columna "Puntaje" de trend-map |
| Brief | Routine `02-borradores` | Notion, estado "Brief" |
| Borrador | Routine `02-borradores` + skills | Notion, estado "Borrador" |
| Aprobás | **Vero** | Notion, estado "Aprobado" |
| Programa | Vero (o Routine cuando haya scheduler conectado) | Buffer / Metricool |

## Control
- **Cola de aprobación:** vista de Notion filtrada por estado = Borrador.
- **Log de actividad:** `orchestrator/activity-log.md` (cada Routine agrega una línea).
- **Botón de apagado:** desactivar las Routines desde claude.ai/code → Routines, o pedirle a Claude que las pause.

## Cómo activar las Routines
Pedile a Claude en una sesión de este repo: "activá las routines del orquestador".
Los prompts están en `orchestrator/routines/`. Necesitan los conectores Notion y Windsor.ai.
