# Escenarios de simulación NRP · 9.ª edición

Material educativo independiente preparado para **Dr. Eduardo Velasco · EDUVESA**. Flashcards en español de las **lecciones 2 a 7** del kit aportado. Versión 1.3, 7 de octubre de 2026.

## Abrir sin conexión

1. Descarga y descomprime `NRP9_Escenarios_GitHub.zip`.
2. Abre `index.html` con un navegador moderno.
3. Puedes desconectar internet: contenido, estilos, búsqueda, filtros, registro y guiones están dentro del archivo.

No necesita instalación, servidor, cuentas, dependencias, CDN ni conexión a una API. Los enlaces externos de referencia sí requieren internet. En móviles, abre el archivo en un navegador que ejecute JavaScript; algunas vistas previas de gestores de archivos no lo hacen.

**Offline significa abrir una copia descargada.** Este proyecto no instala un service worker ni promete conservar una página web remota en caché. Visitar GitHub Pages una vez no garantiza acceso posterior sin internet.

## Contenido

| Lección | Tema | Habilidades | Prácticas | Simulaciones originales |
|---|---|---:|---:|---:|
| 2 | Anticipación y preparación | 1 | 2 | 1 |
| 3 | Pasos iniciales | 1 | 4 | 1 |
| 4 | Ventilación y mascarilla laríngea | 1 | 3 | 1 |
| 5 | Intubación y obstrucción de vía aérea | 1 | 2 | 1 |
| 6 | Compresiones | 1 | 1 | 1 |
| 7 | Acceso vascular, adrenalina y volumen | 1 | 1 | 1 |
| **Subtotal original** | **25 tarjetas** | **6** | **13** | **6** |

Cada tarjeta contiene consigna, equipo, tareas individuales, guía oculta del instructor, criterios de logro y debriefing. Los casos incluyen fases con información que revela el instructor y respuesta esperada. Las habilidades se presentan por lección; en un caso breve se marcan solo las acciones realmente observadas.

Se incluye búsqueda, filtros, selección aleatoria, reloj docente, cuatro alumnos con nombres editables, rotaciones, notas, evaluación formativa, exportación JSON/CSV e impresión de una tarjeta o de toda la selección. El registro genera constancias educativas de escenario o lección; no determina por sí mismo la aprobación de un curso NRP.

## Usarlo en una estación

1. Selecciona lección y tarjeta de **Habilidad**. El instructor demuestra; cada alumno practica según su rol profesional.
2. En parejas A–B y C–D, intercambia operador y asistente. En técnicas avanzadas se ejecuta o se asiste dentro del ámbito autorizado.
3. Selecciona una tarjeta de **Práctica**. En esta fase se permite orientación y corrección inmediata.
4. Selecciona una **Simulación**. Realiza prebriefing, asigna funciones y explica las limitaciones del maniquí. El instructor revela hallazgos sin anticipar la próxima maniobra.
5. Abre la guía del instructor en su dispositivo o imprime el guion; no la proyectes a los alumnos durante el escenario. Ocultarla es una ayuda docente, no una barrera de acceso.
6. Cambia el alumno seleccionado antes de marcar tareas y registrar resultados. Todos deben liderar una ronda y demostrar las destrezas pertinentes; observar no sustituye practicar.
7. Realiza debriefing: reacción breve, reconstrucción, análisis mediante observación e indagación y compromiso de mejora. Repite la habilidad que necesite refuerzo.
8. Exporta el registro antes de cerrar o cambiar de dispositivo.

Las funciones de la tabla de rotación son orientativas. El líder debe redistribuirlas según el personal real y la complejidad; en reanimación avanzada puede requerirse personal adicional. El reloj solo mide tiempo docente, no controla el algoritmo ni programa cambios automáticos en el paciente.

## Archivos

- `index.html`: aplicación completa, autónoma y lista para servir como página principal.
- `README.md`: instrucciones de uso, alcance y publicación.
- `contenido.json`: copia estructurada y editable de las lecciones y tarjetas.
- `sincronizar_contenido.py`: inserta cambios de `contenido.json` en `index.html`; Python 3, sin paquetes adicionales.
- `NOTAS_CLINICAS.md`: decisiones editoriales, limitaciones y puntos para revisión del instructor.
- `.nojekyll`: permite servir el contenido como sitio estático sin procesamiento Jekyll.

El PDF fuente no está incluido. No se añaden logotipos ni una licencia abierta sobre contenidos de terceros.

## Prepararlo para GitHub

Este ZIP es un proyecto listo para subir; **no crea un repositorio remoto ni publica en un portal automáticamente**.

1. Crea o elige un repositorio de GitHub.
2. Sube los archivos descomprimidos a la raíz: `index.html` debe quedar en la raíz, no dentro de un ZIP.
3. Confirma los cambios en la rama que utilizarás para publicar.
4. Si deseas una URL web, configura GitHub Pages para servir la rama y carpeta que contienen `index.html`, según las opciones disponibles en tu cuenta.
5. Conserva también la copia local para uso sin conexión.

En un portal que acepte contenido estático, coloca `index.html` en la carpeta de publicación. Para modificar el portal existente se necesita conocer su repositorio, URL y estructura.

No subas registros de alumnos, pacientes, credenciales ni el PDF del kit a un repositorio público. Revisa tus permisos sobre cualquier material adicional antes de publicarlo.

## Guardado y privacidad

El progreso usa `localStorage` si el navegador lo permite. En algunos navegadores, modo privado o archivos `file://`, el almacenamiento puede estar limitado. La app muestra un aviso si no puede guardar.

El registro es local: no se transmite, no se sincroniza y puede perderse al borrar datos, mover el archivo o cambiar de navegador. Usa iniciales cuando convenga y exporta una copia. El JSON exportado es un respaldo legible; esta versión no incluye importación de registros. El CSV abre en una hoja de cálculo e incluye el estado de todas las tarjetas por alumno.

## Editar contenidos

Edita `contenido.json` y ejecuta desde la carpeta del proyecto:

```bash
python3 sincronizar_contenido.py
```

El script comprueba estructura básica, identificadores únicos y referencias a lecciones, y actualiza los datos embebidos. No valida exactitud médica. Revisa el contenido con un instructor cualificado y vuelve a probar la página antes de distribuir cambios. Para modificar apariencia o funciones, edita directamente el HTML.

## Fuentes y atribución

Fuente principal: archivo aportado por el usuario **NRP_9ed_Kit_Instructor_ES_COMPLETO(3).pdf**, 86 páginas. Los números de página de las tarjetas corresponden al archivo PDF, no a la paginación reiniciada de cada sección.

| Material fuente | Páginas PDF |
|---|---|
| Constructor de escenarios | 9–10 |
| Instrucciones y plantilla de escenarios | 11–27 |
| Lección 2 | 28–32 |
| Lección 3 | 33–40 |
| Lección 4 | 41–52 |
| Lección 5 | 53–63 |
| Lección 6 | 64–69 |
| Lección 7 | 70–77 |

Consulta complementaria: [AHA/AAP, 2025 Guidelines, Part 5: Neonatal Resuscitation](https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines/neonatal-resuscitation), consultada el 6 de octubre de 2026.

Las prácticas son adaptaciones resumidas y las seis simulaciones están identificadas como propuestas originales. No se presentan como formularios oficiales ni como reproducción completa del ITK. El alcance termina en la lección 7; no incluye un curso completo de todas las lecciones del manual.

NRP es una marca de la American Academy of Pediatrics. Material independiente sin implicar aprobación de AAP/AHA. Uso educativo con maniquí y supervisión; no sustituye el manual vigente ni los protocolos institucionales.

## Comprobaciones de esta entrega

Se comprobó la sintaxis de JavaScript, la presencia de las 38 tarjetas (13 prácticas), los datos embebidos y la ausencia de recursos de ejecución remotos. No fue posible completar una prueba visual en navegador en el entorno de generación. Antes del primer curso, abre la copia local y verifica filtros, revelado del instructor, registro y exportación en el dispositivo que utilizarás.

## Simulaciones del ITK añadidas · versión 1.1

El ITK exige simulación con debriefing en el curso; no establece una lista única de escenarios obligatorios por lección. La agenda permite reutilizar prácticas seleccionadas o construir escenarios según los objetivos. Los casos siguientes son **adaptaciones para simulación integrada de las variantes de práctica del kit**, no nuevos formularios oficiales. La aplicación contiene ahora **38 tarjetas: 6 de habilidades, 13 prácticas, 6 simulaciones originales y 13 simulaciones ITK**.

| Lección | Variantes ITK para seleccionar | Tarjetas | Páginas PDF |
|---|---|---:|---|
| 2 | Preparación de un nacimiento de bajo riesgo / de 29 semanas | 2 | 28–32 |
| 3 | Término vigoroso / meconio y cianosis / respuesta a pasos iniciales / prematuro tardío apneico | 4 | 33–40 |
| 4 | Ventilación con riesgo conocido / apnea inesperada / mascarilla laríngea | 3 | 41–52 |
| 5 | Intubación / obstrucción con necesidad de aspiración traqueal | 2 | 53–63 |
| 6 | Bradicardia persistente que requiere compresiones | 1 | 64–69 |
| 7 | Prolapso de cordón: CVU, adrenalina y rama de volumen si está indicada | 1 | 70–77 |

Seleccione **Simulación ITK** en el filtro Actividad. Cada nueva tarjeta agrega objetivos, respuestas a las cuatro preguntas previas, referencia al documento, instrucciones de facilitación sin orientación, guion condicionado a las acciones y debriefing.

La lección 2 adapta ejercicios de preparación: el Constructor comienza en la lección 3. El caso de apnea de lección 3 debe continuar inmediatamente hacia ventilación cuando se realiza una simulación integrada; el punto de cierre de la práctica aislada no debe interrumpir la atención real. Las opciones de CPAP, sonda OG, volumen, sangre y acceso intraóseo dependen de los objetivos y de la indicación; no son obligatorias en todo escenario.

El Constructor sugiere factores de riesgo por complejidad: lección 3, hipertensión/ausencia de control prenatal/prematuridad; lección 4, preeclampsia/magnesio/restricción de crecimiento/meconio cuando corresponda; lección 5, patrón fetal categoría III/fiebre/presentación anómala; lección 6, eclampsia/extracción por vacío fallida/bradicardia fetal; lección 7, cesárea urgente y anestesia general, añadiendo evidencia plausible de pérdida sanguínea si se pretende evaluar volumen. Son ejemplos de construcción, no datos que obliguen automáticamente a una intervención.

La simulación incluye habilidades conductuales en todas las lecciones. El facilitador registra decisiones y acciones y reserva el análisis para el debriefing. Fuentes: pp. 1–5, 9–10 y 11–27, además de las páginas de cada lección.

## Narrativa clínica en cada tarjeta · versión 1.2

Las 38 tarjetas incluyen ahora una narrativa clínica para preparar y presentar el caso. La guía del instructor agrega el estado inicial del recién nacido, la evolución prevista, notas sobre los límites del caso y respuestas a las cuatro preguntas previas en las variantes del kit. Las tarjetas de habilidad muestran un caso de referencia y botones para abrir las otras variantes de la lección. Los seis escenarios originales conservan esa identificación.

Los datos obstétricos se entregan cuando se solicitan; los signos neonatales se revelan en la fase correspondiente. No agregar edad materna, peso, vía del parto o diagnóstico como si fueran datos del kit cuando no están especificados. La versión (3) del PDF aportado contiene el mismo contenido que la versión (2) utilizada anteriormente.

## Evaluación y certificados · versión 1.3

1. Seleccione el alumno e introduzca su nombre completo. Añada el instructor evaluador, la entidad emisora y la fecha en «Métricas, avance y certificados».
2. Indique el rol individual. Puntúe cada acción: **2 correcta sin ayuda; 1 correcta con ayuda; 0 incorrecta**. «No observado» queda pendiente. «No aplica» requiere justificar por qué la acción no corresponde al caso o al rol. Las casillas antiguas siguen siendo un registro de práctica; no se convierten automáticamente en notas.
3. La calificación es `100 × puntos obtenidos / (2 × acciones aplicables)`. Las acciones no observadas siguen en el denominador. Una exclusión justificada se retira. La cobertura es el porcentaje de acciones aplicables que ya fueron evaluadas. No puede certificarse una evaluación sin acciones puntuables.
4. Finalización satisfactoria: nota **≥80%**, cobertura **100%**, todos los puntos críticos aplicables con **2**, datos de identificación, rol y cierre del instructor. Puede cerrar una evaluación insuficiente para conservarla; no habilita el certificado. La nota no es una regla oficial del ITK/AAP/AHA ni una escala validada. Los puntos críticos son una selección editorial visible en cada tabla.
5. Descargue el certificado en **PDF directo**, sin conexión ni dependencias. La opción **HTML** incluye el detalle de acciones, puntos, justificaciones y evidencia; permite imprimir o guardar como PDF desde el navegador.
6. Para certificar una lección, se reúne la evidencia **más reciente** de cada competencia entre las rondas actuales, sin sumar competencias duplicadas. Todas deben tener una puntuación observada en una evaluación cerrada. Una acción «No aplica» en un escenario no acredita la competencia de la lección. Use la ficha de habilidad u otro caso para evaluarla. No se exige completar todas las variantes de escenarios.
7. Cualquier modificación de la evaluación, del rol, del nombre del alumno o de los datos de emisión invalida el cierre afectado hasta revisarlo de nuevo. «Nueva ronda» conserva la anterior en el historial del registro JSON. El certificado describe la ronda actual; no certifica una trayectoria acumulada ni resultados de otros alumnos.
8. Exporte el JSON como respaldo (incluye rúbrica e historial) y el CSV detallado para revisar acciones y notas. Los archivos PDF/HTML descargados son instantáneas; no se actualizan ni revocan automáticamente al cambiar el registro local.

El certificado es una **constancia educativa de EDUVESA**. No constituye eCard, certificación NRP de AAP/AHA, acreditación de proveedor avanzado ni autorización clínica. No incorpora firma digital, validación de identidad ni consulta externa; el instructor es responsable de la evaluación declarada.
