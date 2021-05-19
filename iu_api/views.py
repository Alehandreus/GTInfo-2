from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserOnlineActivityObjectSerializer
from .models import UserOnlineActivityObject


class UserOnlineActivityObjectViewSet(viewsets.ModelViewSet):
    """
    Отвечает за просмотр и редактирование текущей истории
    """
    queryset = UserOnlineActivityObject.objects.all()
    serializer_class = UserOnlineActivityObjectSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
