from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

@app.get("/dados")
def resposta():
    return {"mensagem": "resposta do FastAPI"}

@app.get("/consumir-csharp")
def consumir_csharp():
    try:
        resposta = httpx.get("http://localhost:5001/dados")
        return {"resposta_do_c-sharp": resposta.json()}

    except Exception as e:
        return JSONResponse(content = {"erro": str(e)}, status_code = 500)
