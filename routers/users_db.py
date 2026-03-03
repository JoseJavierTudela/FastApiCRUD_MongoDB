from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemes.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId


router = APIRouter(prefix="/userdb", 
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})


def search_user(field: str, key):
    """Search for a user in the database by field name and value.
    Returns a `User` instance or `None`.
    """
    try:
        record = db_client.users.find_one({field: key})
        if record:
            return User(**user_schema(record))
        return None
    except Exception:
        return None


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
  
    if search_user("email", user.email) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario ya existe")

    user_dict = user.dict()
    user_dict.pop("id", None)  
    inserted = db_client.users.insert_one(user_dict)
    id = inserted.inserted_id
    record = db_client.users.find_one({"_id": id})
    new_user = user_schema(record) if record else None

    return User(**new_user)  

@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())

@router.get("/{id}")  # Path
async def user(id: str):
    return search_user("_id", ObjectId(id))

@router.get("/")  # Query
async def user(id: str):
    return search_user("_id", ObjectId(id))

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):

    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se ha eliminado el usuario"}
    
@router.put("/", response_model=User)
async def user(user: User):

    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error": "No se ha actualizado el usuario"}

    return search_user("_id", ObjectId(user.id))