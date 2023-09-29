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

@app.route("/get-user-nfts", methods=["GET"])
def get_nfts():
    address = request.args.get("address")
    chain = request.args.get("chain")
    params = {
        "address": address,
        "chain": chain,
        "format": "decimal",
        "limit": 100,
        "token_addresses": [],
        "cursor": "",
        "normalizeMetadata": True,
    }

    result = evm_api.nft.get_wallet_nfts(
        api_key=api_key,
        params=params,
    )

    # converting it to json because of unicode characters
    data = json.dumps(result, indent=4)
    response = json.loads(s=data)
    print(response)
    return response


@app.route("/")
def hello_world():
    return {"message": "Hello, Flask!"} 

if __name__ == "__main__":
    app.run(host="192.168.43.166", port=5000, debug=True)
