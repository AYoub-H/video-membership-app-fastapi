import pathlib

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from cassandra.cqlengine.management import sync_table

from app import db
from app.users.models import User

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / "templates"

main_app = FastAPI()
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))

DB_SESSION = None


@main_app.get("/", response_class=HTMLResponse)
def alive(request: Request):
    context = {
        "request": request,
        "abc": 123,
    }
    return templates.TemplateResponse("home.html", context)


@main_app.get("/login", response_class=HTMLResponse)
def login_view(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("auth/login.html", context)


@main_app.on_event("startup")
def on_startup():
    # triggered when fastapi starts
    global DB_SESSION
    DB_SESSION = db.get_session()
    sync_table(User)
