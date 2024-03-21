import uvicorn
from fastapi import FastAPI
from routes.todos_route import todo_api_router

app = FastAPI()

app.include_router(todo_api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)

