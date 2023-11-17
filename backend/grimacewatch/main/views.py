from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import permissions
from web3 import Web3
from web3.contract import Contract
from dexscreener import DexscreenerClient
import requests
from .models import History
from additional.helpers import *
from rest_framework.generics import ListAPIView

from .serializers import HistorySerializer


class HistoryListView(ListAPIView):
    queryset = History.objects.all()[::-1]
    serializer_class = HistorySerializer
    permission_classes = [permissions.AllowAny]


class ListTokens(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        """
        Return a list of all users.
        """

        try:
            client = DexscreenerClient()
            

            POST_DATA = {

            }
            print(request.data)
            address=Web3.to_checksum_address(request.data["address"])
            balance = get_balance(address)
            grimace_amount = get_grimace_balance(address)
            pair = client.get_token_pair("dogechain", "0x1aAD352a2190B399Bb3cfD4d5E4B0bf6EFA33C0e")
            POST_DATA["GRIMACE"] = {
                    "quantity": grimace_amount,
                    "price": pair.price_usd,
                    "balance": pair.price_usd * grimace_amount
                }
            total = grimace_amount * pair.price_usd
            for (name, info) in PAIR_DATA.items():
                pair = client.get_token_pair("arbitrum", info)
                total += pair.price_usd * balance[name]
                POST_DATA[name] = {
                    "quantity": balance[name],
                    "price": pair.price_usd,
                    "balance": pair.price_usd * balance[name]
                }
            
            History.objects.create(
                address=address,
                total=total
            )


            POST_DATA = sorted(POST_DATA.items(), key=lambda x: x[1]["balance"], reverse=True)

            # pair = client.get_token_pair("arbitrum", "0xa5Dd76C46dE4d800ca9F985105A36b1F3ABF7969")
            # pairs = client.get_token_pairs("0xa5Dd76C46dE4d800ca9F985105A36b1F3ABF7969")
            # GRIMACE = client.get_token_pair("dogechain", "0x1aAD352a2190B399Bb3cfD4d5E4B0bf6EFA33C0e")
            # print(pair)
            return Response({"data": POST_DATA, "total" :total})
        
        except ValueError:
            return Response({"error": "not found"})