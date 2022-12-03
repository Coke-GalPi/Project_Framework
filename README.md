# Este es el repositorio para el proyecto de FLP, con el framework FastAPI

## Descaragar VS Code y Python 3.10.8
    
    VS Code:

        https://code.visualstudio.com/Download

    Python:

        https://www.python.org/ftp/python/3.10.8/python-3.10.8-amd64.exe

    Extensiones:

        Python Extension Pack.

        Code Runner.

## Pasos para usar FastAPI.

    1.- Crear un entorno virtual

        Asegurar tener la libreria "virtualenv" para crear el entorno.

            Comando para crear el entrono virtual: "virtualenv -p python3 [nombre del entorno]"

            Comando para entrar: ".\[nombre entrono]\Scripts\activate"

            Comando para salir: "deactivate"

    Una vez dentro del entrono virtual debe instalar las siguientes librerias:

    2.- Debe instalar la libreria de fastapi por terminal de VS Code

        pip install fastapi

    3.- Debe instalar uvicorn

        pip install uvicorn

    4.- Esto instalará uvicorn con dependencias mínimas (Python puro).

        pip install uvicorn[standard] 

    5.- Otras librerias 

        pip install autopep8

        pip install jinja2 //gestor de plantillas

## Para ejecutar el codigo debe utilizar el comando:

    uvicorn main:app --reload

## Documentación:

    Python: 

        https://docs.python.org/es/3.10/

    fastAPI:

        https://fastapi.tiangolo.com

    uvicorn:

        https://www.uvicorn.org