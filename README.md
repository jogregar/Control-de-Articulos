# Control de Artículos

Esta es una pequeña aplicación web para controlar el inventario de artículos. La aplicación está construida con Djago y permite conectarse a una base datos MySQL y gestionarla desde la la app.

## Características

- Conectarse con una base de datos MySQL.
- Agregar, consultar, modificar y eliminar artículos.
- Agregar, consultar, modificar y eliminar categorías.

## Requisitos Previos

- Python 3.6 o superior.
- pip (gestor de paquetes de Python).
- Django (Framework para Python).
- base de datos db.sqlite3

## Instalación

Siga estos pasos para instalar y ejecutar la aplicación en su entorno local:

### 1. Clonar el Repositorio

Primero, clone el repositorio en su máquina local:

```bash
git clone https://github.com/jogregar/Control-de-Articulos.git
```
```bash
cd Control-de-Inventario
```

### 2. Crear y Activar un Entorno Virtual

Cree un entorno virtual para gestionar las dependencias de Python:

```bash
py -m venv crud-venv
```

Active el entorno virtual. El comando para activar el entorno virtual depende de su sistema operativo:

* Windows:
```bash
.\crud-venv\Scripts\activate
```
* macOS / Linux:
```bash
source crud-venv/bin/activate
```  

### 3. Instalar las Dependencias

Con el entorno virtual activado, instale las dependencias del proyecto:
```bash
pip install -r requirements.txt
``` 

### 4. Instalar MySQL

Puede descargaqr MySQL desde su sitio web oficial o bien utilizar algun servidor apache como xamp, laragon, etc. Despues de descargar e instalar MySQL debe ejecutar sus servicios, esto dependera de la aplicación seleccionada para utilizar.

### 5. Crear base de datos y tablas

El archivo respaldo_inventerio.sql contiene un respado de la base de datos, el mismo creara la base de datos junto con las tablas necesarias.

Para este paso se debe estar ejecutando los servicios de MySQL. Proceda a ejecutar el siguiente comando desde la consola.
```bash
mysql -u root -p < respaldo_inventario.sql
```

### 6. Ejecutar la Aplicación
Inicie la aplicación:
```bash
py manage.py runserver
```
o
```bash
python3 app.py
```

La aplicación estará disponible en http://127.0.0.1:8000/ o http://localhost:8000. Abra cualquiera de estos enlaces en su navegador web.

## Uso

### Cargar la app

1. Acceda a la interfaz web. Para ello abra su navegador y en la url proceda a escribir http://127.0.0.1:8000/ o http://localhost:8000 
2. Use el menú de navegación para acceder a las diferentes opciones de la app

### Estructura de Archivos

* `myapp/models.py`: Contiene todos los modelos para interactuar con la aplicación Django.
* `myapp/views.py`: Contiene todas las funciones que rendizaran los templates.
* `myapp/templates/index.html`: La plantilla HTML para la interfaz web.
* `myapp/templates/articulos.html`: La plantilla que muestra todos los articulos. 
* `myapp/templates/admin-articulos.html`: La plantilla que permite registrar o modificar los articulos. 
* `myapp/templates/categorias.html`: La plantilla que muestra todas las categorias. 
* `myapp/templates/admin-categorias.html`: La plantilla que permite registrar o modificar las categorias. 

## Realizado Por

Este proyecto fue realizado por alumnos de quinto año de informática 2024 del Colegio del Carmen:

- ALVAREZ VARGAS, AUGUSTO
- ARIAS, FERNANDO JEREMIAS
- BERNABE VELILLA, JUAN PABLO
- BUCHTER, JOAQUIN SEBASTIAN
- CALVO DEMURU, VALENTINO HUGO
- CASANOVA, JUAN MARCO
- DUBROWSKY, EZEQUIEL
- GARRIDO, AGUSTÍN
- GATICA SOSA, LUCIANO BENJAMÍN
- GIORDANO, TADEO
- GOMEZ HERNANDEZ, MÁXIMO
- MANCHADO, JUAN IGNACIO
- MATARAZZO MATOZ, CHIARA ADRIANA
- MAZZAMATI , JUAN PABLO
- MOYANO YAÑEZ, FACUNDO NICOLÁS
- OLMEDO, LUCIANO FRANCISCO
- ORLANDO BRAS, JOSEFINA

**¡Gracias por su contribución!**

### Guiado por:
* **[José G. García A.](https://github.com/jogregar)**


