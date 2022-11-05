from fastapi import FastAPI
import diccionarios


app = FastAPI()


@app.get("/2019")
async def dict1():
    return diccionarios.dict_2019


@app.get("/2020")
async def dict1():
    return diccionarios.dict_2020


@app.get("/2021")
async def dict1():
    return diccionarios.dict_2021