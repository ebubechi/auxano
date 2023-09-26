
from moralis import evm_api
from fastapi import FastAPI, Request

app = FastAPI()


api_key = "KVUjiwZZQHfBN3ttK7lPeSmmWdsAq2yyoDGfB12qkmqpoWrfjwWsH478ewzmk4n3"

@app.get("/get-token-balance")
async def get_token_balance(req : Request):
    chain = req.query_params.get("chain")
    address = req.query_params.get("address")
    params = {
    "chain": chain,
    "address": address
    }

    result = await evm_api.balance.get_native_balance(
    api_key=api_key,
    params=params,
    )

    return result




@app.get("/")
def read_root():
    return {"Hello" : "FastAPI"}
