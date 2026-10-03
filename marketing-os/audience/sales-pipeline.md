# Pipeline de ventas

El tramo que el diagrama original no tiene: de la conversación al cliente.
Vive en Google Sheets (planilla "Máquina de marketing", pestaña "Pipeline"); este archivo define las etapas.

| Etapa | Sister | BRIDGE | Qué la mueve |
|---|---|---|---|
| Conversación | Comentario o DM | Comentario, DM o conexión | `linkedin-comment-engine`, `bridge-prospecting` |
| Valor entregado | Ebook freemium | Mensaje de valor / reto de 21 días | Kit + `bridge-prospecting` |
| Discovery | — | Llamada agendada (Google Calendar) | Invitación suave al terminar el reto |
| Propuesta | — | Propuesta enviada | Vero |
| Cliente | Compra libro / curso | Contrato firmado | Vero |

**Columnas:** Nombre · Empresa · Rol · Línea · Etapa · Origen (post, comentario, newsletter, Sales Nav) · Próximo paso · Fecha.
El campo **Origen** es lo que permite saber qué contenido vende (ver `analytics/attribution.md`).
