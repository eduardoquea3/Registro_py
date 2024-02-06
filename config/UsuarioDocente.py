from .database import db, collection
from bson import ObjectId
from fastapi import HTTPException


def get_all():
    client = db()
    coll = collection(client, "Registro", "UsuarioDocente")
    docs = coll.find()
    # all_items = list(docs)
    all_items = [{"_id": str(doc["_id"]), "name": doc.get("name")}
                 for doc in docs]
    client.close()
    return all_items


async def get_one_user(id: str):
    try:
        client = db()
        coll = collection(client, "Registro", "UsuarioDocente")
        usr = ObjectId(id)
        crt = {"_id": usr}
        doc = coll.find_one(crt)
        if doc:
            return doc
        else:
            raise HTTPException(
                status_code=404, detail="usuario no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
