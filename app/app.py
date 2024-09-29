import fastapi
from schema import CreateTodo, ItemId, GetTodo, UpdateTodo, StatusResponse
from lifespan import lifespan

app = fastapi.FastAPI(
    title="ToDO API",
    description="ToDo API",
    version="1.0.0",
    lifespan=lifespan
)


@app.get('/v1/todo', response_model=GetTodo)
async def get_todo(todo_id: int):
    return {}


@app.post('/v1/todo', response_model=ItemId)
async def create_todo(todo: CreateTodo):
    return {}


@app.put('/v1/todo/{todo_id}', response_model=ItemId)
async def update_todo(todo_id: int, todo: UpdateTodo):
    return {}


@app.delete('/v1/todo/{todo_id}', response_model=StatusResponse)
async def delete_todo(todo_id: int):
    return {'status': 'deleted'}
