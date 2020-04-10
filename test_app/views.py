from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class TestView(APIView):

    def post(self, request, format=None):
        try:
            data = request.data
            a = data.get("a")
            b = data.get("b")
            return Response({"Total":int(int(a)+int(b))},status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"msg":str(e)})






