
# Biblioteca API

## Descripción

Este es un proyecto de API RESTful para gestionar una pequeña biblioteca. La API permite realizar las siguientes operaciones sobre libros:

- Agregar libros con título, autor, año de publicación e ISBN.
- Listar todos los libros o filtrarlos por autor o año.
- Actualizar la información de un libro.
- Eliminar un libro.
- Buscar libros por título o autor.

La API está construida usando **FastAPI**, y utiliza **PostgreSQL** como base de datos. El ORM utilizado es **SQLAlchemy**.

## Tecnologías utilizadas

- **FastAPI**: Framework para crear la API.
- **SQLAlchemy**: ORM para interactuar con la base de datos PostgreSQL.
- **PostgreSQL**: Base de datos relacional.
- **Docker**: Para contenerizar la aplicación.
- **Pytest**: Para pruebas unitarias y de integración.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación FastAPI.
- **Pydantic**: Para validaciones y serialización de datos.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- [Python 3.10 o superior](https://www.python.org/)
- [Docker](https://www.docker.com/get-started)
- [PostgreSQL](https://www.postgresql.org/)

## Instalación

### 1. Clonar el repositorio

Clona el repositorio a tu máquina local:

```bash
git clone https://github.com/alejomjc/biblioteca_api.git
cd biblioteca_api
```

### 2. Crear un entorno virtual y activarlo

Crea un entorno virtual y actívalo:

```bash
python -m venv env
source env/bin/activate  # En Windows usa: env\Scripts\activate
```

### 3. Instalar dependencias

Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

### 4. Configurar las bases de datos

Debes configurar dos bases de datos PostgreSQL:

1. **`biblioteca`**: Es la base de datos para el proyecto principal.
2. **`test_biblioteca`**: Es la base de datos para realizar las pruebas.

Puedes crearlas ejecutando los siguientes comandos en PostgreSQL:

```bash
psql -U postgres -c "CREATE DATABASE biblioteca;"
psql -U postgres -c "CREATE DATABASE test_biblioteca;"
```

### 5. Configuración de la base de datos

La conexión a la base de datos se gestiona de la siguiente manera:

- **Base de datos para el proyecto** (`biblioteca`): Se encuentra en el archivo `app/models.py`.
- **Base de datos para las pruebas** (`test_biblioteca`): Se encuentra en el archivo `app/tests/test_api.py`.

**En `app/models.py`**:
```python
SQLALCHEMY_DATABASE_URL = "postgresql://your_user:your_password@localhost/biblioteca"
```

**En `app/tests/test_api.py`**:
```python
SQLALCHEMY_DATABASE_URL = "postgresql://your_user:your_password@localhost/test_biblioteca"
```

## Ejecución

### 1. Ejecutar la aplicación con Docker

Para ejecutar la aplicación usando Docker, puedes construir y correr el contenedor:

```bash
docker build -t biblioteca-api .
docker run -p 8000:8000 biblioteca-api
```

### 2. Ejecutar la aplicación localmente (sin Docker)

Si prefieres ejecutar la aplicación localmente sin Docker, usa el siguiente comando:

```bash
uvicorn app.main:app --reload
```

Esto levantará el servidor en `http://localhost:8000`.

### 3. Acceder a la documentación de la API

Una vez que la aplicación esté corriendo, puedes acceder a la documentación generada automáticamente por FastAPI en:

- [http://localhost:8000/docs](http://localhost:8000/docs) para la documentación interactiva de la API.
- [http://localhost:8000/redoc](http://localhost:8000/redoc) para la documentación estática de la API.

## Pruebas

### 1. Ejecutar las pruebas con Pytest

Para ejecutar las pruebas unitarias e integradas del proyecto, puedes usar Pytest. Asegúrate de que la base de datos `test_biblioteca` esté configurada antes de ejecutar las pruebas.

```bash
pytest
```

Esto ejecutará todas las pruebas definidas en el directorio `app/tests`.
