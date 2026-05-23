## Indicaciones

1. Crear las entidades en función de clases.py
2. Crear un archivo que permita poblar la base de datos; usar los csv's dados

Orden sugerido de carga:

- 01_departamento.csv
- 02_instructor.csv
- 03_curso.csv
- 04_estudiante.csv
- 05_inscripcion.csv
- 06_tarea.csv
- 07_entrega.csv

3. Generar los siguiente archivos

* consulta1.py: Listas las entregas, presentar por cada entrega: nombre del estudiantes, titulo, nombre del profesor
* consulta2.py: Listar los cursos, obtener los cursos profesores en su nombre tengan la cadena "Zam"
* consulta3.py: Listar las inscripciones del departamento de Ciencias de la Computación. Por cada inscripción, presentar el nombre del estudiante, el nombre del curso y el nombre del profesor
* consulta4.py: Por cada curso, presentar sus tareas asociadas.

# EJECUCIÓN - Ejemplo 03

## Actividades realizadas

Se trabajó con los archivos CSV proporcionados y el archivo `clases.py` ya existente.
La carpeta quedó organizada de la siguiente manera:

![alt text]({B59529E0-1CAA-48B5-AD06-5588BAE455A8}.png)


### Creación de `ingreso_datos.py`

Se creó el archivo `ingreso_datos.py` que lee los 7 archivos CSV en el orden correcto
y los carga en la base de datos respetando las relaciones entre tablas (llaves foráneas).

Tomamos en cuenta las dependencias para poder hacer una carga valida:
1. `01_departamento.csv` — sin dependencias
2. `02_instructor.csv` — sin dependencias
3. `03_curso.csv` — depende de Departamento e Instructor
4. `04_estudiante.csv` — sin dependencias
5. `05_inscripcion.csv` — depende de Estudiante y Curso
6. `06_tarea.csv` — depende de Curso
7. `07_entrega.csv` — depende de Tarea y Estudiante

Se usa `csv.DictReader` para leer cada archivo y se hace `commit` luego de cada
entidad para garantizar que los registros existan antes de cargar los que dependen de ellos.


### Creación de las consultas

#### `consulta1.py`
Lista todas las entregas. Por cada entrega muestra:
- Nombre del estudiante
- Título de la tarea
- Nombre del profesor


#### `consulta2.py`
Lista los cursos cuyos profesores tienen la cadena `"Zam"` en su nombre.
Se usa `.join(Instructor).filter(Instructor.nombre.like("%Zam%"))`.

#### `consulta3.py`
Lista las inscripciones del departamento **Ciencias de la Computación**.
Por cada inscripción muestra el nombre del estudiante, el nombre del curso y el nombre del profesor.
Se encadenan los joins: `Inscripcion → Curso → Departamento`.

#### `consulta4.py`
Por cada curso lista sus tareas asociadas, navegando la relación `curso.tareas`
definida en `clases.py`.


## Capturas de ejecuciones locales

### Creación de tablas e ingreso de datos

![alt text]({A51A5BA1-1706-413D-89E7-8D209013739A}.png)

### Consulta 1 — Entregas con estudiante, tarea y profesor

![alt text]({BA260108-2688-43C0-814A-ECC3C10E8BC1}.png)

### Consulta 2 — Cursos con profesor que contiene "Zam"

![alt text]({969EB456-4095-48FA-AC3F-271BEB9B7B77}.png)

### Consulta 3 — Inscripciones de Ciencias de la Computación

![alt text]({1F573D6E-B06F-4F1B-81D9-D69067313F25}.png)

### Consulta 4 — Tareas por curso

![alt text]({219562FA-ACD7-4FD0-A45C-D6235860B029}.png)