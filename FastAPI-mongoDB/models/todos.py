from pydantic import BaseModel

# validator and used as a database table


class Todo(BaseModel):
    name: str
    description: str
    completed: bool
