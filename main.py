from fastapi import FastAPI, Request, Response, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from werkzeug.security import generate_password_hash
from connection import DAO
from check_data_user import check_data_user

app = FastAPI(title="Proyecto Framework fastAPI",
            description="Proyecto para el ramo 'FLP'",
            version="1.0.1")

dao = DAO()

template = Jinja2Templates(directory="./view")

@app.get("/", response_class=HTMLResponse) # Index
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})
@app.post("/", response_class=HTMLResponse) # Index
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})

@app.get("/signin", response_class=HTMLResponse) # Login
def signin(req: Request):
    return template.TemplateResponse("signin.html", {"request": req})
@app.post("/signin", response_class=HTMLResponse) # Login
def signin(req: Request):
    return template.TemplateResponse("signin.html", {"request": req})

@app.post("/user")      # access user
async def user(req: Request, username: str = Form(), password_user: str = Form()):
    verify = check_data_user(username+"@estudiantesunap.cl", password_user)
    if verify:
        return template.TemplateResponse("user.html", {"request": req, "data_user": verify})
    return RedirectResponse("/")

@app.get("/signup", response_class=HTMLResponse) # Registro de nuevo Usuario
def signup(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})
@app.post("/signup", response_class=HTMLResponse) # Registro de nuevo Usuario
def signup(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})

@app.post("/data_users")  # insert new user
async def data_users(name: str = Form(), lastname: str = Form(), rut: str = Form(), 
                fono: str = Form(), username: str = Form(), password_user: str = Form()):
    data_user = [rut, name, lastname, fono, username+"@estudiantesunap.cl", generate_password_hash(password_user)]
    dao.insert_new_User(data_user)
    return RedirectResponse("/")

@app.post("/insert_doc")  # insert new doc
async def insert_doc(type_doc: str = Form(), teacher_doc: str = Form(), name_doc: str = Form(),
                    theme_doc: str = Form(), file_doc: str = Form()):
    data_document = [type_doc, teacher_doc, name_doc, theme_doc, file_doc]
    dao.insert_new_Document(data_document)
    return RedirectResponse("/signin")

@app.get("/search_theme")   # search of doc
def search_theme(req: Request, theme: str = Form()):
    data_doc = dao.search_document(theme)
    return data_doc

@app.get("/contact", response_class=HTMLResponse) # contacto
def contact(req: Request):
    return template.TemplateResponse("contact.html", {"request": req})