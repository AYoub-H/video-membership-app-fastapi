from fastapi import FastAPI
from cassandra.cqlengine.management import sync_table

from app import db
from app.users.models import User

main_app = FastAPI()
DB_SESSION = None


@main_app.get("/")
def alive():
    return {"message": "hello world"}


@main_app.on_event("startup")
def on_startup():
    # triggered when fastapi starts
    global DB_SESSION
    DB_SESSION = db.get_session()
    sync_table(User)
