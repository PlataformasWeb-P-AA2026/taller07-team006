import csv
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import cadena_base_datos
from clases import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def parse_dt(valor):
    """Convierte string a datetime, retorna None si está vacío."""
    if valor and valor.strip():
        return datetime.strptime(valor.strip(), "%Y-%m-%d %H:%M:%S")
    return None

# ── 01 Departamentos ──────────────────────────────────────────────────────────
with open("01_departamento.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        session.add(Departamento(id=int(row["id"]), nombre=row["nombre"]))
session.commit()
print("Departamentos cargados.")

# ── 02 Instructores ───────────────────────────────────────────────────────────
with open("02_instructor.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        session.add(Instructor(id=int(row["id"]), nombre=row["nombre"]))
session.commit()
print("Instructores cargados.")

# ── 03 Cursos ─────────────────────────────────────────────────────────────────
with open("03_curso.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        session.add(Curso(
            id=int(row["id"]),
            titulo=row["titulo"],
            departamento_id=int(row["departamento_id"]),
            instructor_id=int(row["instructor_id"])
        ))
session.commit()
print("Cursos cargados.")

# ── 04 Estudiantes ────────────────────────────────────────────────────────────
with open("04_estudiante.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        session.add(Estudiante(id=int(row["id"]), nombre=row["nombre"]))
session.commit()
print("Estudiantes cargados.")

# ── 05 Inscripciones ──────────────────────────────────────────────────────────
with open("05_inscripcion.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        session.add(Inscripcion(
            estudiante_id=int(row["estudiante_id"]),
            curso_id=int(row["curso_id"]),
            fecha_inscripcion=parse_dt(row["fecha_inscripcion"])
        ))
session.commit()
print("Inscripciones cargadas.")

# ── 06 Tareas ─────────────────────────────────────────────────────────────────
with open("06_tarea.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        session.add(Tarea(
            id=int(row["id"]),
            curso_id=int(row["curso_id"]),
            titulo=row["titulo"],
            fecha_entrega=parse_dt(row["fecha_entrega"])
        ))
session.commit()
print("Tareas cargadas.")

# ── 07 Entregas ───────────────────────────────────────────────────────────────
with open("07_entrega.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        session.add(Entrega(
            id=int(row["id"]),
            tarea_id=int(row["tarea_id"]),
            estudiante_id=int(row["estudiante_id"]),
            fecha_envio=parse_dt(row["fecha_envio"]),
            calificacion=float(row["calificacion"]) if row["calificacion"].strip() else None
        ))
session.commit()
print("Entregas cargadas.")

print("\nBase de datos poblada correctamente.")
