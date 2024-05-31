from fastapi import FastAPI
import TMService as service

app = FastAPI()

@app.get("/list")
async def list():
    return service.list()

@app.post("/create")
async def list():
    return service.create()

@app.patch("/update")
async def list():
    return service.update()

@app.post("/upsert")
async def list():
    return service.upsert()

@app.delete("/delete")
async def list():
    return service.delete()