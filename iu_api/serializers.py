from .models import UserOnlineActivityObject, TrackedUserObject
from rest_framework import serializers


class UserOnlineActivityObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOnlineActivityObject
        fields = ['tracked_user', 'started_playing_timestamp', 'ended_playing_timestamp', 'game_id', 'total_played']


class TrackedUserObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackedUserObject
        fields = ['steam_id']