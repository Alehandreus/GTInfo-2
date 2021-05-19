from .models import UserOnlineActivityObject
from rest_framework import serializers


class UserOnlineActivityObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOnlineActivityObject
        fields = ['steam_id', 'started_playing_timestamp', 'ended_playing_timestamp', 'game_id', 'total_played']
