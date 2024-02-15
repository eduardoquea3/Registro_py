from fastapi import APIRouter
from ..config.UsuarioDocente import get_all, get_one_user
from ..models.user import User

app = APIRouter()


@app.get("/usuario", tags=["Usuario Docente"])
def users() -> list[User]:
    all_items = get_all()
    return all_items


@app.get("/usuario/{id}", tags=["Usuario Docente"])
def user(id: str):
    get_user = get_one_user(id)
    return get_user
