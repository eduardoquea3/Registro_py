from ..models.user import User


def validate_user(user:dict) -> User:
  user["_id"]=str(user["_id"])
  validation = {
    "id": user["_id"],
    "name": user["name"],
    "apellidoP": user["apellidoP"],
    "apellidoM": user["apellidoM"],
    "correo": user["correo"],
    "contra": user["contra"],
  }
  return User(**validation)


def adding_user(user:User)->dict:
  del user.id
  return dict(user)