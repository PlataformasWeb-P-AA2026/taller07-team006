from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# -----------------------------------------------
# Ingreso de Clubs desde data/datos_clubs.txt
# Formato: nombre;deporte;fundacion
# -----------------------------------------------
with open("data/datos_clubs.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            partes = linea.split(";")
            nombre = partes[0]
            deporte = partes[1]
            fundacion = int(partes[2])
            club = Club(nombre=nombre, deporte=deporte, fundacion=fundacion)
            session.add(club)

# Se confirman los clubs para poder consultarlos al agregar jugadores
session.commit()

# -----------------------------------------------
# Ingreso de Jugadores desde data/datos_jugadores.txt
# Formato: club_nombre;posicion;dorsal;nombre_jugador
# Nota: algunas líneas no tienen dorsal (ej: "Layan Loer"), se maneja el caso
# -----------------------------------------------
with open("data/datos_jugadores.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            partes = linea.split(";")
            # Verificar si el dorsal es un número o si falta
            if len(partes) == 4:
                club_nombre = partes[0]
                posicion = partes[1]
                dorsal = int(partes[2])
                nombre_jugador = partes[3]
            else:
                # Línea con formato incompleto (sin dorsal)
                club_nombre = partes[0]
                posicion = partes[1]
                dorsal = 0
                nombre_jugador = partes[2]

            # Buscar el club por nombre para asignar la relación
            club = session.query(Club).filter_by(nombre=club_nombre).one()

            jugador = Jugador(
                nombre=nombre_jugador,
                dorsal=dorsal,
                posicion=posicion,
                club=club
            )
            session.add(jugador)

# Se confirman todos los jugadores
session.commit()

print("Datos ingresados correctamente.")
print("Clubs y jugadores guardados desde los archivos de datos.")
