from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

class DetailViewServiceA(APIView):
    def get(self, request, format = None):
        return Response(data = "Hello ServiceA", status = HTTP_200_OK)

class DetailViewServiceB(APIView):
    def get(self, request, format = None):
        return Response(data = "Hello ServiceB", status = HTTP_200_OK)