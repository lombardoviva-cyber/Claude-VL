# Routine 05 · Lote semanal de Instagram

**Cuándo:** lunes 11:45 (después de la Routine 02).
**Conectores:** Google Drive.

## Prompt
```
Sos el orquestador del Marketing OS de Vero Lombardo (repo Claude-VL).
1. Leé marketing-os/distribution/instagram-cuentas.md y trabajá solo las cuentas con estado "activa".
2. Para cada cuenta, leé research/trend-map.md, content/hook-bank.md y la skill de voz que indica la tabla.
   Usá la skill instagram-content-engine para decidir formato, largo, cantidad de placas y caption.
3. Elegí los temas de la semana: primero reciclá las ideas aprobadas de LinkedIn de la semana anterior,
   después los temas mejor puntuados que encajen en los pilares de esa cuenta.
4. Para cada pieza escribí una fila en la pestaña "Instagram" de la planilla "Máquina de marketing":
   Cuenta · Fecha propuesta · Formato · Hook · Placa 1 … Placa 8 (texto corto por placa) · Guion de reel
   (si es reel, con tiempos) · Caption · Texto alternativo · Estado = "Borrador".
   Las columnas de placas son las que lee la plantilla de Canva para crear los diseños en lote.
5. Si una cuenta tiene menos de 3 piezas aprobadas para la semana siguiente, avisalo arriba del log.
6. Agregá una línea a orchestrator/activity-log.md. Commit y push.
No publiques ni diseñes nada: Vero aprueba primero.
```

## Paso 2 (martes, después de la aprobación)
En una sesión con Claude: "armá en Canva las piezas aprobadas de Instagram".
Claude toma las filas con Estado = "Aprobado", crea los diseños con la plantilla de cada cuenta,
genera la versión para stories y TikTok cuando corresponde, y deja los links en la columna "Diseño".
