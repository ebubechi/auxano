from flask import Flask, request
from moralis import evm_api
import json


app = Flask(__name__)


api_key = "KVUjiwZZQHfBN3ttK7lPeSmmWdsAq2yyoDGfB12qkmqpoWrfjwWsH478ewzmk4n3"

@app.route("/get-token-balance", methods=["GET"])
def get_token_balance():
    chain = request.args.get("chain")
    address = request.args.get("address")
    params = {
    "chain": chain,
    "address": address
    }

    result = evm_api.balance.get_native_balance(
    api_key=api_key,
    params=params,
    )

    return result


@app.route("/")
def hello_world():
    return {"message": "Hello, Flask!"} 