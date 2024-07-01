# EspoCRM Demo Automation

Automatización de pruebas para la versión demo de EspoCRM, enfocada en los módulos de equipos y usuarios utilizando
pytest con la libreria de requests en pyhton.

## Descripción

Este proyecto automatiza las pruebas para la versión demo de EspoCRM, enfocándose en los módulos de equipos y usuarios.
Utiliza como lenguaje de programacion Python con pytest aprovechando con la libreria de requets para escribir y ejecutar
las pruebas.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura:

```bash 
├── src
│ ├── assertions
│ ├── espocrm_api
│ ├── resources
│ ├── utils
├── tests
│ ├── equipos
│ ├── usuarios
├── config.py
├── conftest.py
└── README.md
```

- `src/assertions`: Contiene las aserciones utilizadas en los test cases.
- `src/espocrm_api`: Contiene las peticiones de requests y los endpoint que se utilizaran.
- `src/resources`: Contiene los esquemas para validar los esquemas que devuelve y la autentificacion para utilizar en
  los test cases.
- `src/utils`: Contiene varias utilidades para el proyecto.
- `tests/equipos`: Test cases para el módulo de equipos.
- `tests/usuarios`: Test cases para el módulo de usuarios.
- `config.py`: Archivo de configuración.
- `conftest.py`: Archivo de configuración para pytest, la peticion del login.

## Instalación

### Requisitos previos

- Python 3.12.2
- pip
- IDE (recomendado Pycharm)

### Instrucciones

1. Clona el repositorio y navega al directorio del proyecto:

    ```bash
    git clone https://github.com/AutenticosDecadentes/EspoCRM_Automation.git
    cd EspoCRM_Automation
    ```

2. Crea un entorno virtual e instala las dependencias:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `.\venv\Scripts\activate`
    pip install pytest requests jsonschema pytest-html
    ```

## Ejecución de Tests

Para ejecutar los tests, sigue estos pasos:

1. Clona este repositorio y cambia a la rama `develop`:
    ```bash
    git clone https://github.com/AutenticosDecadentes/EspoCRM_Automation.git
    cd EspoCRM_Automation
    git checkout develop
    ```

2. Crea un entorno virtual y activa el entorno:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `.\venv\Scripts\activate`
    pip install pytest requests jsonschema pytest-html
    ```

3. Ejecuta los test cases con el comando:
    ```bash
    pytest -v
    ```

   Para generar un informe en HTML:
    ```bash
    pytest -v --html=report.html --self-contained-html
    ```
   Para visualizar el informe de HTML abrir en el navegador de su preferencia el archivo generado, recomendado Chrome:
    ```bash
    report.html
    ```

## Referencias

- Documentacion de EspoCRM: https://docs.espocrm.com/
- Demo de EspoCRM: https://demo.us.espocrm.com/
