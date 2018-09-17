from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserInfo
from .serializer import UserInfoSerialiser
from django.http import Http404
from rest_framework import status

from django.conf import settings

# model = settings.MODEL


class UserInfoView(APIView):

    # def index():
    #     print("Predicting")
    #     res = model.predict(numpy.stack([test_img]))
    #     print(res)

    def get(self, request):
        userInfo = UserInfo.objects.all()
        userInfo = UserInfoSerialiser(userInfo, many=True)
        return Response(userInfo.data)

    def post(self, request, format=None):
        serializer = UserInfoSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
