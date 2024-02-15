from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: str
    name: str
    apellidoP: Optional[str] = None
    apellidoM: Optional[str] = None
    correo: Optional[str] = None
    contra: Optional[str] = None
