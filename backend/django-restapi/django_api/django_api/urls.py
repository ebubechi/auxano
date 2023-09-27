"""
URL configuration for django_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.urls import path
from moralis import evm_api
import json


api_key = "KVUjiwZZQHfBN3ttK7lPeSmmWdsAq2yyoDGfB12qkmqpoWrfjwWsH478ewzmk4n3"

@api_view(["GET"])
def get_token_balance(req):
    chain = req.GET["chain"]
    address = req.GET["address"]
    params = {
    "chain": chain,
    "address": address
    }

    response = evm_api.balance.get_native_balance(
    api_key=api_key,
    params=params,
    )

    return Response(response)

@api_view(["GET"])
def get_user_nfts(req):
    address = req.GET["address"]
    chain = req.GET["chain"]
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
    response = json.loads(data)
    print(response)
    return Response(response)


@api_view(['GET', 'POST'])
def hello_world(req):
    if req.method == 'POST':
        return Response({"message": "created something", "data": req.data})
    return Response({"message": "Hello, Django Rest Api"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('get-token-balance/', get_token_balance),
    path('get-user-nfts/', get_user_nfts),
]
