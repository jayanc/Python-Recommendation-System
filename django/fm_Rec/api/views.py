from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserInfo
from .serializer import UserInfoSerialiser
from django.http import Http404
from rest_framework import status
import numpy
from django.conf import settings

from .fm_predictions import display_recommended_items, product_train
model = settings.MODEL


class UserInfoView(APIView):

    def get(self, request):
        userInfo = UserInfo.objects.all()
        userInfo = UserInfoSerialiser(userInfo, many=True)
        return Response(userInfo.data)

    def post(self, request, format=None):
        print("request.data", request.data['user_id'])

        display_recommended_items(
            model, product_train, request.data['user_id'])

        serializer = UserInfoSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
