from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World! 我的网站已上线！"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"你好 {name}!"}