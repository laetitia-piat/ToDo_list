from fastapi import FastAPI
from app.routers.todo import router as todo_router

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(todo_router)