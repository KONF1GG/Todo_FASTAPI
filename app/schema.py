from pydantic import BaseModel
from datetime import datetime
from typing import Literal


class GetTodo(BaseModel):
    id: int
    title: str
    description: str
    importance: bool
    created_at: datetime
    done: bool


class ItemId(BaseModel):
    id: int


class CreateTodo(BaseModel):
    title: str
    description: str
    importance: bool


class UpdateTodo(BaseModel):
    title: str | None = None
    description: str | None = None
    importance: bool | None = None
    done: bool | None = None


class StatusResponse(BaseModel):
    status: Literal['success', 'deleted']
