from contextlib import asynccontextmanager
from fastapi import FastAPI
from models import engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('START')
    async with engine.begin() as conn:
        await conn.run_sunc(Base.metadata.create_all())
    yield
    print('STOP')