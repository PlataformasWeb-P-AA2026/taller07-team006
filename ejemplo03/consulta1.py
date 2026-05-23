from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import cadena_base_datos
from clases import Entrega, Tarea, Curso, Instructor, Estudiante

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Listar todas las entregas
# Por cada entrega: nombre del estudiante, título de la tarea, nombre del profesor
entregas = session.query(Entrega).all()

print("=== Listado de Entregas ===\n")
for entrega in entregas:
    estudiante = entrega.estudiante.nombre
    titulo_tarea = entrega.tarea.titulo
    profesor = entrega.tarea.curso.instructor.nombre
    print("Estudiante : %s" % estudiante)
    print("Tarea      : %s" % titulo_tarea)
    print("Profesor   : %s" % profesor)
    print("-" * 50)
