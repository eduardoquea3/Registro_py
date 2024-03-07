from .database import db, collection
from bson import ObjectId
from fastapi import HTTPException
from ..models.user import User
from ..schemas.user import validate_user,adding_user


def get_all() -> list[User]:
    client = db()
    coll = collection(client, "Registro", "UsuarioDocente")
    docs = coll.find()
    all_items = []
    for doc in docs:
        all_items.append(validate_user(doc))
    client.close()
    return all_items


def get_one_user(id: str):
    try:
        client = db()
        coll = collection(client, "Registro", "UsuarioDocente")
        crt = {"_id": ObjectId(id)}
        doc = coll.find_one(crt)
        if doc:
            return validate_user(doc)
        else:
            raise HTTPException(
                status_code=404, detail="usuario no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def add_user(user:User)->User:
    client=db()
    coll = collection(client, "Registro", "UsuarioDocente")
    new = adding_user(user)
    result = coll.insert_one(new)
    id = result.inserted_id
    new["_id"]=id
    return validate_user(new)

def delete_user(id:str):
    result = collection(db(), "Registro", "UsuarioDocente").delete_one(
        {"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"mesage": "Documento eliminado exitosamente"}
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")


def update_user(id: str, user: User):
    del user.id
    item = collection(db(), "Registro", "UsuarioDocente").find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)})
    if item:
        return validate_user(item)
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
