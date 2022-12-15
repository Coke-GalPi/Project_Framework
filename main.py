from fastapi import FastAPI, Request, Response, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from model.db_connection import Connection


app = FastAPI()
conn = Connection()

template = Jinja2Templates(directory="./view")

@app.get("/", response_class=HTMLResponse) # Index
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})

@app.get("/signin", response_class=HTMLResponse) # Login
def signin(req: Request):
    return template.TemplateResponse("signin.html", {"request": req})

@app.get("/signup", response_class=HTMLResponse) # Registro de Usuario
def signup(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})

@app.get("/contact", response_class=HTMLResponse) # Perfil de Usuario
def user(req: Request):
    return template.TemplateResponse("contact.html", {"request": req})
