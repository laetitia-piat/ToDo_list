from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.todo import TodoCreate, TodoRead
from app.crud.todo import create_todo, get_todos

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=list[TodoRead])
def read_todos(db: Session = Depends(get_db)):
    return get_todos(db)

@router.post("/", response_model=TodoRead)
def create_todo_endpoint(
    todo: TodoCreate,
    db: Session = Depends(get_db)
):
    return create_todo(db, todo)
