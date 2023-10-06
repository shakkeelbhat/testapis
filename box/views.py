from django.shortcuts import render
from rest_framework.views import APIView
from .serializers  import registerSerializer, loginSerializer, boxSerializer
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class registerApi(APIView):
    def post(self,request):

        try:
            data  = request.data
            serializer  = registerSerializer(data=data)
            if not serializer.is_valid():
                return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'message':'User registered'},status=status.HTTP_200_OK)
        except:
            return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)



class loginApi(APIView):
    pass

class listApi(APIView):
    pass

class addApi(APIView):
    pass

