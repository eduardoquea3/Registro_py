from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(
    "mongodb://root:saitama123@localhost:27017/?authSource=Registro")
database = client.Registro
UsuarioDocente = database.UsuarioDocente


async def get_one_user(id):
    user = await UsuarioDocente.find_one({"_id": id})
    return user


async def create_user(user):
    new_user = await UsuarioDocente.insert_one(user)
    created_user = await UsuarioDocente.find_one({"_id": new_user.inserted_id})
    return created_user
