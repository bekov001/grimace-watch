from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import permissions
from web3 import Web3
from web3.contract import Contract
from dexscreener import DexscreenerClient
import requests
from .models import History, Tokens
from additional.helpers import *
from rest_framework.generics import ListAPIView

from .serializers import HistorySerializer


class HistoryListView(ListAPIView):
    queryset = History.objects.all().order_by("-id")
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
            

            POST_DATA = {

            }
            print(request.data)
            address=Web3.to_checksum_address(request.data["address"])
            balance = get_balance(address)
            grimace_amount = get_grimace_balance(address)

            tokens = Tokens.objects
            GRIMACE = tokens.filter(name="GRIMACE").latest("id")
            POST_DATA["GRIMACE"] = {
                    "quantity": grimace_amount,
                    "price":  GRIMACE.price,
                    "balance": GRIMACE.price * grimace_amount
                }
            total = grimace_amount *  GRIMACE.price
            for (name, info) in PAIR_DATA.items():
                token = tokens.filter(name=name).latest("id")
                total += token.price * balance[name]
                
                POST_DATA[name] = {
                    "quantity": balance[name],
                    "price": token.price,
                    "balance": token.price * balance[name]
                }
            print(tokens.filter(name=name).last())
            History.objects.create(
                address=address,
                total=total
            )


            POST_DATA = sorted(POST_DATA.items(), key=lambda x: x[1]["balance"], reverse=True)
            return Response({"data": POST_DATA, "total" :total})
        
        except ValueError:
            return Response({"error": "not found"})