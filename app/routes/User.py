from fastapi import APIRouter
from ..config.UsuarioDocente import (
    get_all, get_one_user, add_user, delete_user, update_user)
from ..models.user import User
# from fastapi.encoders import jsonable_encoder

app = APIRouter()


@app.get("/usuario", tags=["Usuario Docente"])
def users() -> list[User]:
    all_items = get_all()
    return all_items


@app.get("/usuario/{id}", tags=["Usuario Docente"])
def user(id: str):
    get_user = get_one_user(id)
    return get_user


@app.post("/usuario", tags=["Usuario Docente"])
def add(user: User):
    new_user = add_user(user)
    return new_user


@app.delete("/usuario/{id}", tags=["Usuario Docente"])
def delete(id: str):
    return delete_user(id)


@app.put("/usuario/{id}", tags=["Usuario Docente"])
def update(id: str, user: User):
    return update_user(id, user)
