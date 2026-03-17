from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, UserProfile, Workout


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'universe']


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'team']


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration_minutes', 'calories_burned', 'performed_at']


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user', 'score', 'rank']


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'user', 'title', 'intensity', 'scheduled_for', 'completed']
