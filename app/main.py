from fastapi import FastAPI

main_app = FastAPI()


@main_app.get("/")
def alive():
    return {"hello": "world"}
