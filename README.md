# Proyecto de gestion de hotel

_El siguiente es un un miservicio _

## Comenzando 🚀

_Para poder reproducir este microservicio y acceder a su codigo fuente, unicamente debes clonar el repositorio y acceder a la carpeta backend_

_Para desplegar el proyecto local o remotamente debes tener en cuenta las instrucciones encontradas en el apartado **Instalacion** y **Ejecución de microservicio**._

### Pre-requisitos 📋

_Principalmente se requiere instalar python (ideal 3.8 o superior) y git bush para realizar la copia del proyecto (En su defecto descargar el proyecto como zip), una vez clonado el repositorio accede a back_end y realiza el procedimiento descrito en **Instalación** y  **Pruebas**._

### Instalación 🔧

_Inicialmente crea tu entorno virtual dentro de la carpeta **back_end**, para ello accede al folder back_end en tu editor, inicia una terminal e inserta el siguiente comando_
```
python -m venv env
```

_Activa el entorno virtual con:
```
env/Scripts/activate
```
_Para Linux._
```
source env/bin/activate
```

_Con el entorno virtual instalado Añade las librerias requeridas dentro del entorno virtual._

```
pip3 install -r requirements.txt
```

## Ejecutando el microservicio ⚙️

_A continuacion se describe la forma de realizacion de las pruebas locales, posterior a ello se explicara como realiar el despliegue y las pruebas remotas_

### Configuraciond de base de datos

_Previo a la ejecución del microservicio y la realizacion de pruebas es necesario definir la conexion a la base de datos, para ello en el archivo **settings.py** debemos editar el diccionario llamado **DATABASES** con los datos del esquema y la base de datos a realizar la conexion, preferiblemente el esquema debe estar vacio_

_Posterior a la configuracion de la base de datos, se deben generar las migraciones._
```
python manage.py makemigrations
```

_Finalmente se debe realizar la migracion._
```
python manage.py migrate
```

### Ejecución local del microservicio 🔩

_Si no tienes abierto el entorno virtual debes ejecutarlo_
```
env/Scripts/activate
```

_Ejecuta el microservicio para ello debes ejecutar_
```
python manage.py runserver
```

## Despliegue 📦

_Esta es una guia para desplegar el microservicio a heroku._

### Requisitos

_Es necesario haber realizado los pasos mostrados en los apartados **prerequisitos** e **instalacion**_

_Debes tener instalado **heroku cli** en tu equipo y tener una cuenta en heroku._

_Debes instalar Docker en caso de que no lo hayas hecho_

### Despliegue del microservicio

_Iniciar sesion con heroku cli._
```
heroku login
```

_Conectar el Docker con heroku_
```
heroku container:login
```
 
_Crear imagen del microservicio, para esto necesitas tener una app creada dentro de heroku, representada con nombre_app_
```
heroku container:push web --app nombre_app
```

_Finalmente ya podemos realizar el despliegue con_
```
heroku container:release web --app nombre-app
```

## Ejecucion de pruebas

_En el documento **PruebasBitacora2.pdf** se encuentra la descripcion a detalle sobre la realizacion de pruebas_

## Construido con 🛠️

_Pricipalmente el proyecto se desarrollo con el lenguaje python, con ayuda del framework Django_

* [python](https://www.python.org) - Lenguaje Usado
* [django](https://www.djangoproject.com) - Framework usado
