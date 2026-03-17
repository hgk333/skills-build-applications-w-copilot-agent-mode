from django.contrib import admin

from .models import Activity, LeaderboardEntry, Team, UserProfile, Workout


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'universe')
    search_fields = ('name', 'universe')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'team')
    list_filter = ('team',)
    search_fields = ('name', 'email')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'activity_type', 'duration_minutes', 'calories_burned', 'performed_at')
    list_filter = ('activity_type',)
    search_fields = ('user__name', 'activity_type')


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'score', 'rank')
    list_filter = ('rank',)
    search_fields = ('user__name',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'intensity', 'scheduled_for', 'completed')
    list_filter = ('intensity', 'completed')
    search_fields = ('user__name', 'title')
