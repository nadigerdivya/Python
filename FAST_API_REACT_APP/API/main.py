from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

class TransactionBase(BaseModel) :
    amount: float
    category: str
    description: str
    is_income: bool
    date: str

class TransactionModel(TransactionBase):
    id: int

    class Config:
        from_attributes = True

#create db connection

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Ensure database tables are created
models.Base.metadata.create_all(bind=engine)

#### API End points ####

# Create transaction
@app.post("/transactions/", response_model=TransactionModel)
async def create_transaction(transaction: TransactionBase, db: db_dependency):
    ## get the transaction object, map and store it in database
    db_transaction = models.Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)  # ✅ Ensures `id` is populated
    return db_transaction 

#Get Transactions
@app.get("/transactions", response_model=List[TransactionModel])
async def get_transactions(db: db_dependency, skip: int = 0, limit:int = 100):
    transactions = db.query(models.Transaction).offset(skip).limit(limit).all()
    return transactions
