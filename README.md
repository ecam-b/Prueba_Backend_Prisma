# Prueba_Backend_Prisma

### Descripción del proyecto
En este proyecto se realiza la creación de una API REST por medio del lenguaje de programación Python, junto al framework Flask, usando SQLAlchemy para la conexión y gestión de la base de datos alojada en el motor PostgreSQL. Por lo que fue necesario el uso del adaptador Psycopg2 para dicha conexión.

Para el serializado de los documentos JSON se utilizo la libreria Marshmallow, con las capas de compatibilidad flask-marshmallo y marshmallo-sqlalchemy.

Ademas se usaron las librerias python-decouple python-dotenv para entender y acceder a variables de entorno, permitiendo aislar los valores necesarios para la conexión al servidor.

#### Estructura del proyecto

Por medio de los Blueprints de flask se realizó una División estructural, en donde el codigo se divide por modulos dependiendo la funcionalidad. Creando directorios para los modelos, las rutas, la conexión a la base de datos y para las utilizades.

Se crea al archivo config.py para la lectura de las variables de entorno y configuraciones de la base de datos, ademas se crea el archivo app.py que sera el archivo base para ejecutar la aplicación.

    src/
        database/
        models/
        routes/
        utils/
        app.py
        config.py

#### Creación de las tablas

Para la creación de las tablas se emplean los modelos trabajados con SQLAlchemy, en donde se establecen todos los atributos con sus respectivos parametros sin necesidad de escribir codigo en SQL, solo usando la sintaxis del ORM trabajado. Ademas se establecen los esquemas para enseñar los objetos JSON serializado.

```py
class UserModel(db.Model):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True, nullable=False)
  username = db.Column(db.String(50))
  passw = db.Column(db.String(500))
  email = db.Column(db.String(100))
  bills = db.relationship("BillModel")

  def __init__(self, username, passw, email):
    self.username = username
    self.passw = passw
    self.email = email


class UserSchema(ma.Schema):
  class Meta:
    fields = ("id", "username", "passw", "email")
```

## Despliege de la aplicación
Se deben seguir los siguientes pasos:
##### Descargar repositorio
```sh
git clone https://github.com/ecam-b/Prueba_Backend_Prisma.git
```

Una ves descargado se ingresa a la carpeta con:
```sh
cd Prueba_Backend_Prisma
```

##### Instalación de python3-venv
```sh
sudo apt install -y python3-venv
```
##### Creación del entorno virtual
```sh
python3 -m venv env
```
##### Activación del entorno virtual
```sh
source env/bin/activate
```
##### Instalación de depentencias por medio del archivo requirements.txt
```sh
pip3 install -r requirements.txt
```
### Creación de variables de entorno
Para la conexión de la aplicación en necesario crear un archivo .env que contenga los parametros del servidor y base de datos.

    .env

Que contiene la siguiente variables
```sh
PGSQL_USER = <nombre_user>
PGSQL_PASSWORD = <contaseña>
PGSQL_HOST = localhost
PGSQL_DATABASE = <nombre_database>

SECRET_KEY = <clave-secreta>
```

##### Lanzamiento de la aplicación
```sh
python3 src/app.py
```
##### PostgreSQL
Desde pgAdmin 4 se observara como se crearon las tablas 'users' y 'bill'. Para acceder a esa información, visualizarla, crear nuevos datos, eliminarlos y modificarlos se hace uso de herramientas como Postman o Insomnia.
##### Insomnia
Para probar la API se tiene las siguientes rutas con sus respectivos metodos HTTP:

### POST
Registrar un nuevo usuario.
```
http://localhost:5000/login
```
Se le debe pasar un objeto JSON con la estructura:
```json
{
	"username": "usuario",
	"passw": "1234",
	"email": "usuario@gmail.com"
}
```
### GET
Obtener las bills existentes.
```
http://localhost:5000/bills/
```
### POST
Registrar una nueva bill.
```
http://localhost:5000/bills/
```
Se le debe pasar un objeto JSON con la estructura:
```json
{
	"date_bill": "2022-01-18",
	"user_id": 1,
	"value": 300,
	"type": 1,
	"observation": "Ninguna observación"
}
```
### DELETE
Eliminar una bill por medio de su 'id'.
```
http://localhost:5000/bills/{id}
```
### PUT
Actualizar una bill por medio de su 'id'.
```
http://localhost:5000/bills/{id}
```
Se le debe pasar un objeto JSON con la estructura:
```json
{
	"date_bill": "2023-01-18",
	"user_id": 1,
	"value": 200,
	"type": 2,
	"observation": "Ninguna observación"
}
```