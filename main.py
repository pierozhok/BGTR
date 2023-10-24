from fastapi import FastAPI
from routers import router

app = FastAPI()

@app.get('/')
def hello():
    return "hello world! it's working!"

@app.get('/home/test1/{parameter}')
def name(parameter: str):
    return "path parameter test: " + parameter

@app.get('/home/test2')
def session(parameter: str):
    return "query parameter test: " + parameter

app.include_router(router)
