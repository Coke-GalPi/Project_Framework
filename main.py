from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from model.db_connection import Connection

app = FastAPI()
conn = Connection()

template = Jinja2Templates(directory="./view")

@app.get("/", response_class=HTMLResponse)
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})

@app.get("/signin", response_class=HTMLResponse)
def signin(req: Request):
    conn
    return template.TemplateResponse("signin.html", {"request": req})

@app.get("/signup", response_class=HTMLResponse)
def signup(req: Request):
    conn
    return template.TemplateResponse("signup.html", {"request": req})