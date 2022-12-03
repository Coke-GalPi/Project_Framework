from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

template = Jinja2Templates(directory="./view")

@app.get("/", response_class=HTMLResponse)
def root(req: Request):
    return template.TemplateResponse("login.html", {"request": req})

@app.get("/signup", response_class=HTMLResponse)
def signup(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})

@app.get("user", response_class=HTMLResponse)
def user(req: Request):
    return template.TemplateResponse("user.html", {"request": req})

