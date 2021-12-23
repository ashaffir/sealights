from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from django.contrib.auth.models import User
from .serializers import UserSerializer


class AddUser(GenericAPIView):
    """add user (dev)"""

    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)
