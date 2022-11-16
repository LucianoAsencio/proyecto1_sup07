from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
import diccionarios


app = FastAPI()


# @app.get("/items", response_class=HTMLResponse)
# async def read_items():
#     return """
#     <html>
#         <head>
#             <title>LuchitoAPI</title>
#         </head>
#         <body>
#             <h1>Diccionarios de Netflix</h1>
#             <h2>Luchito API</h2>
#             <ul>
#                 <lh>Diccionarios</lh>
#                 <li><a href="/2019">Diccionario 2019</a></li>
#                 <li><a href="/2020">Diccionario 2020</a></li>
#                 <li><a href="/2021">Diccionario 2021</a></li>
#         </body>
#     </html>
#     """

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