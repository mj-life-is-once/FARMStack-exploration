from typing import Annotated, List

import models
from database import SessionLocal, engine
from fastapi import Depends, FastAPI  # , HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# validate the request from react application
class TransactionBase(BaseModel):
    amount: float
    category: str
    description: str
    is_income: bool
    data: str


class TransationModel(TransactionBase):
    id: int

    # https://stackoverflow.com/questions/75211183/what-does-pydantic-orm-mode-exactly-do
    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        # create a db connection (when the request comes in)
        yield db
    finally:
        # if we don't find the connection, close it
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
models.Base.metadata.create_all(bind=engine)


@app.post("/transactions", response_model=TransationModel)
async def create_transcation(transaction: TransactionBase, db: db_dependency):
    # unpack everything from the transaction dictionary
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


# skip (start from) and limit (end at) are optional parameters
@app.get("/transactions", response_model=List[TransationModel])
async def read_transactions(db: db_dependency, skip: int = 0, limit: int = 100):
    transactions = db.query(models.Transaction).offset(skip).limit(limit).all()
    return transactions
