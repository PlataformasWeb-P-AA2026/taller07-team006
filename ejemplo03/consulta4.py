from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import cadena_base_datos
from clases import Curso

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Por cada curso, presentar sus tareas asociadas
cursos = session.query(Curso).all()

print("=== Tareas por Curso ===\n")
for curso in cursos:
    print("Curso: %s" % curso.titulo)
    if curso.tareas:
        for tarea in curso.tareas:
            print("  - %s (entrega: %s)" % (tarea.titulo, tarea.fecha_entrega))
    else:
        print("  (sin tareas registradas)")
    print("-" * 50)
