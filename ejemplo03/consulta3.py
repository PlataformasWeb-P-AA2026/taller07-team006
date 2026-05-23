from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import cadena_base_datos
from clases import Inscripcion, Curso, Departamento, Instructor, Estudiante

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Listar inscripciones del departamento "Ciencias de la Computación"
# Por cada inscripción: nombre del estudiante, nombre del curso, nombre del profesor
inscripciones = session.query(Inscripcion)\
    .join(Curso)\
    .join(Departamento)\
    .filter(Departamento.nombre == "Ciencias de la Computación").all()

print("=== Inscripciones - Ciencias de la Computación ===\n")
for ins in inscripciones:
    print("Estudiante : %s" % ins.estudiante.nombre)
    print("Curso      : %s" % ins.curso.titulo)
    print("Profesor   : %s" % ins.curso.instructor.nombre)
    print("-" * 50)
