# Proyecto FastAPI

## Autor:

    Coke-GalPi


## Descaragar VS Code, Python 3.10.8, DBeaver y PostgreSQL
    
    VS Code:

        https://code.visualstudio.com/Download

    Python:

        https://www.python.org/ftp/python/3.10.8/python-3.10.8-amd64.exe

    DBeaver gestor de Base de Datos

        https://dbeaver.io/files/dbeaver-ce-latest-x86_64-setup.exe

    PostgresSQL:

        https://www.enterprisedb.com/postgresql-tutorial-resources-training?uuid=7ce7e93f-e1eb-4e42-85fa-84c0c98859ee&campaignId=7012J000001h3GiQAI

    Extensiones para VS Code:

        Python Extension Pack.

        Code Runner.

## Pasos para usar FastAPI.

    1.- Crear un entorno virtual

        Asegurar tener la libreria "virtualenv" para crear el entorno.

            Comando para crear el entrono virtual: "virtualenv -p python3 venv"

            Comando para entrar: ".\venv\Scripts\activate"

            Comando para salir: "deactivate"

    2.- Una vez dentro del entrono virtual debe instalar las siguientes librerias:

        Para ahorar los pasos siguientes puedes usar el comando: "pip install -r .\requirements.txt"
        para que se instalen las librerias en la misma version en la que se empieza la programación de este codigo.

        En caso contrario segur con los pasos:

    3.- Debe instalar la libreria de fastapi por terminal de VS Code

        pip install fastapi

    4.- Debe instalar uvicorn

        pip install uvicorn

    5.- Esto instalará uvicorn con dependencias mínimas (Python puro).

        pip install uvicorn[standard] 

    6.- Otras librerias 

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