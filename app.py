from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def model():
    return {"message ": "success"}