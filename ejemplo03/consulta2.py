from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import cadena_base_datos
from clases import Curso, Instructor

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Listar cursos cuyos instructores tengan "Zam" en su nombre
cursos = session.query(Curso).join(Instructor)\
         .filter(Instructor.nombre.like("%Zam%")).all()

print("=== Cursos con profesor que contiene 'Zam' ===\n")
for curso in cursos:
    print("Curso    : %s" % curso.titulo)
    print("Profesor : %s" % curso.instructor.nombre)
    print("-" * 50)
