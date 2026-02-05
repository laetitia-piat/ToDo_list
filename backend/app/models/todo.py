from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    object: Mapped[str] = mapped_column(String(200))
    done: Mapped[bool] = mapped_column(Boolean, default=False)
