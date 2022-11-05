from fastapi import FastAPI
import diccionarios


app = FastAPI()


@app.get("/")
async def index():
    return {'/2019': 'Para ver diccionario de 2019',
            '/2020': 'Para ver diccionario de 2020',
            '/2021': 'Para ver diccionario de 2021'}


@app.get("/2019")
async def dict1():
    return diccionarios.dict_2019


@app.get("/2020")
async def dict1():
    return diccionarios.dict_2020


@app.get("/2021")
async def dict1():
    return diccionarios.dict_2021