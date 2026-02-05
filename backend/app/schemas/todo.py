from pydantic import BaseModel

class TodoCreate(BaseModel):
    object: str
    done: bool = False

class TodoRead(BaseModel):
    id: int
    object: str
    done: bool

    class Config:
        from_attributes = True 
