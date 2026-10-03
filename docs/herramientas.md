# Herramientas: diagrama original vs. tu máquina

El detalle completo, con filtros, está en `docs/maquina-de-marketing.html`.

## Stack mínimo (con lo que ya pagás)
| Pieza | Rol | Estado |
|---|---|---|
| Claude Max + skills | Cerebro, motor de contenido, Routines | Ya pagás |
| Este repo | Capa de conocimiento | Creado |
| Google Workspace | Sheets (calendario, aprobación, pipeline), Drive, Calendar, Meet + notas de Gemini | Ya pagás |
| NotebookLM | Corpus: libro, curso, notas de clientes | Ya pagás |
| Canva Pro | Creativos + Content Planner (LinkedIn perfil y página, IG imagen suelta) | Ya pagás |
| Sales Navigator | Prospección BRIDGE (incluye Premium Business) | Ya pagás |
| Windsor.ai Free | Métricas de 1 fuente: pasar a Instagram | Conectado (hoy: página Método BRIDGE) |
| Kit Free | Newsletter, secuencias, landing | Por sumar |

**Cancelar:** LinkedIn Premium (lo incluye Sales Navigator) y Perplexity Pro (lo cubren Claude Max y Gemini Deep Research). Ahorro: US$50–80/mes.
**Costo nuevo:** US$0 (opcional Windsor.ai Basic US$23 para medir IG y la página de BRIDGE juntas).

## Lo que no hace falta a tu escala
Segment, Supabase, dbt, BigQuery, Airbyte, Sentry, Surfer, Ahrefs, Semrush, Plausible, automatización de X,
publicación masiva. Se reemplazan con Windsor.ai + Claude o directamente no aplican a LinkedIn + Instagram.

## Huecos del flujo original
- **Perfil personal de LinkedIn:** Windsor.ai tiene conectada la página Método BRIDGE, no el perfil. Publicar el perfil → Content Planner de Canva Pro. Métricas del perfil → export mensual manual.
- **Del DM a la venta:** falta el pipeline conversación → discovery → propuesta → cliente (ver `marketing-os/audience/sales-pipeline.md`).
- **Reutilización:** cada idea aprobada sale como post LinkedIn + carrusel IG + bloque de newsletter.
- **Comunidad de Sister:** sin casillero propio todavía.
- **RGPD:** doble opt-in y baja visible para la audiencia de España.
- **IG por Windsor.ai:** solo imágenes sueltas; carruseles y reels a mano (Canva tampoco los programa).
- **Notas de Gemini:** las discoveries grabadas alimentan el ICP con frases textuales de clientes.
- **NotebookLM:** corpus del libro y notas de clientes para research propio.
