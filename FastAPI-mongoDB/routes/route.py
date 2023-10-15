from bson import ObjectId
from config.database import collection_name
from fastapi import APIRouter
from models.todos import Todo
from schema.schemas import list_serial

router = APIRouter()


# GET Request method
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos


# POST Request method
@router.post("/")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))


# PUT Request method
@router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    # overwrite the existing todo
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})


# DELETE Request method
@router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
