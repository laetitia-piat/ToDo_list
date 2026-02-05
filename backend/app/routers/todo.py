from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.todo import get_todos

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/")
def read_todos(db: Session = Depends(get_db)):
    return get_todos(db)
