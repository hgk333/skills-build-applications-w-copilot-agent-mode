from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    universe = models.CharField(max_length=20)

    class Meta:
        db_table = 'teams'
        ordering = ['id']

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='users')

    class Meta:
        db_table = 'users'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} <{self.email}>'


class Activity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    performed_at = models.DateTimeField()

    class Meta:
        db_table = 'activities'
        ordering = ['-performed_at', 'id']

    def __str__(self):
        return f'{self.user.name} - {self.activity_type}'


class LeaderboardEntry(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.PositiveIntegerField()
    rank = models.PositiveIntegerField()

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank', 'id']

    def __str__(self):
        return f'#{self.rank} {self.user.name} ({self.score})'


class Workout(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=120)
    intensity = models.CharField(max_length=20)
    scheduled_for = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'workouts'
        ordering = ['scheduled_for', 'id']

    def __str__(self):
        return f'{self.title} - {self.user.name}'
