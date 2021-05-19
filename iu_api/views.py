from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action

from .serializers import UserOnlineActivityObjectSerializer, TrackedUserObjectSerializer
from .models import UserOnlineActivityObject, TrackedUserObject


class UserOnlineActivityObjectViewSet(viewsets.ModelViewSet):
    """
    Отвечает за просмотр и редактирование списка игровых сессий пользователей
    """
    serializer_class = UserOnlineActivityObjectSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        queryset = UserOnlineActivityObject.objects.all()
        steam_id = self.request.query_params.get("steam_id")
        if steam_id is not None:
            queryset = queryset.filter(tracked_user__steam_id = steam_id)
        return queryset


class TrackedUserObjectViewSet(viewsets.ModelViewSet):
    """
    Отвечает за просмотр и редактирование списка отслеживаемых пользователей
    """
    queryset = TrackedUserObject.objects.all()
    serializer_class = TrackedUserObjectSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

