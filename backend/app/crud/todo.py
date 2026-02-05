from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate

def get_todos(db: Session):
    return db.query(Todo).all()

def create_todo(db: Session, todo: TodoCreate):
    new_todo = Todo(
        object=todo.object, 
        done=todo.done
        )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo
