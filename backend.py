from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"message":"calculator is running"}


@app.get("/add")
def add(a:int,b:int):
    result=a+b
    return {"result":result}

@app.get("/sub")
def sub(a:int,b:int):
    result=a-b
    return {"result":result}

