from .database import db, collection
from bson import ObjectId
from fastapi import HTTPException
from ..models.user import User


def get_all() -> list[User]:
    client = db()
    coll = collection(client, "Registro", "UsuarioDocente")
    docs = coll.find()
    all_items = []
    for doc in docs:
        doc["id"] = str(doc["_id"])
        all_items.append(User(**doc))
    # all_items = [User(**doc) for doc in docs]
    client.close()
    return all_items


def get_one_user(id: str):
    try:
        client = db()
        coll = collection(client, "Registro", "UsuarioDocente")
        crt = {"_id": ObjectId(id)}
        doc = coll.find_one(crt)
        if doc:
            doc["_id"] = str(doc["_id"])
            return doc
        else:
            raise HTTPException(
                status_code=404, detail="usuario no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
