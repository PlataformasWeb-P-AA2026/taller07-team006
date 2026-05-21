## Actividad

* Copiar en esta carpeta los siguientes archivos de la carpeta ejemplo01
	* configuracion.py
	* genera_tablas.py
	* consulta_datos1.py
	* consulta_datos2.py
	* consulta_datos3.py
	* consulta_datos4.py
* Crear un archivo llamado ingreso_datos.py que permita guardar información en las entidades Club y Jugador.
	* Los registros de la clase Club se deben obtener de la carpeta data y el archivo datos_clubs.txt.
	* Los registros de la clase Jugador se deben obtener de la carpeta data y el archivo datos_jugadores.txt.
	* La siguiente consulta, ejemplo, puede ayudar en algún proceso: 

	```python
	session.query(Club).filter_by(nombre="LDU").one()
	```

* Ejecutar los archivos en el orden especificado:
``` sh
python genera_tablas.py
python ingreso_datos.py
python consulta_datos1.py
python consulta_datos2.py
python consulta_datos3.py
python consulta_datos4.py
```
* Verificar que la información obtenida sea la correcta


# EJECUCION
## Actividades realizadas

### Organizacion de archivos 

Se copio y pego los archivos que debian hacerse 
![alt text]({172C4019-9654-4E04-9F5F-42F25414C006}.png)

### Creacion de ingreso de datos

Se creo el archivo ingreso de datos con el cual podemos guardar esta informacion de club y jugador 
De manera mas ordenada que en ejemplo01

### Capturas de ejecuciones locales

![alt text]({F1EDE1A7-3FAD-422E-82A8-325E520C8890}.png)
ejecucion de generacion de tablas e ingreso de datos 

![alt text]({ED8277F5-6E72-41B5-8C14-E66A1EDF94D1}.png)
ejecucion de consulta 1

![alt text]({0E70D528-574A-427B-B3E8-FC7F16D62244}.png)
ejecucion de consulta 2

![alt text]({F184BA3F-B63F-43AD-B67E-5DAD5FC359DD}.png)
ejecucion de consulta 3

![alt text]({D949A997-4554-446C-AC47-31633675AB76}.png)
ejecucion de consulta 4