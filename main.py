from typing import Union
from fastapi import FastAPI
from config.UsuarioDocente import get_all, get_one_user
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/item/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/usuario", tags=["Usuario Docente"])
def users():
    all_items = get_all()
    return all_items


@app.get("/usuario/{id}", tags=["Usuario Docente"])
def user(id: str):
    get_user = get_one_user(id)
    return get_user
