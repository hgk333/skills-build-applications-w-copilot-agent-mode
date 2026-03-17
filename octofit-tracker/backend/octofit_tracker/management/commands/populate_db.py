from datetime import date, timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from octofit_tracker.models import Activity, LeaderboardEntry, Team, UserProfile, Workout


class Command(BaseCommand):
    help = 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'

    @transaction.atomic
    def handle(self, *args, **options):
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Workout.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()

        marvel_team = Team.objects.create(name='Marvel Team', universe='marvel')
        dc_team = Team.objects.create(name='DC Team', universe='dc')

        users = [
            UserProfile.objects.create(name='Peter Parker', email='spiderman@octofit.com', team=marvel_team),
            UserProfile.objects.create(name='Tony Stark', email='ironman@octofit.com', team=marvel_team),
            UserProfile.objects.create(name='Bruce Wayne', email='batman@octofit.com', team=dc_team),
            UserProfile.objects.create(name='Diana Prince', email='wonderwoman@octofit.com', team=dc_team),
        ]

        now = timezone.now()
        activity_rows = [
            (users[0], 'Web Swing Cardio', 45, 430),
            (users[1], 'Power Suit HIIT', 35, 510),
            (users[2], 'Night Run', 50, 470),
            (users[3], 'Amazon Strength', 40, 520),
        ]
        for idx, row in enumerate(activity_rows):
            Activity.objects.create(
                user=row[0],
                activity_type=row[1],
                duration_minutes=row[2],
                calories_burned=row[3],
                performed_at=now - timedelta(days=idx),
            )

        leaderboard_rows = [
            (users[3], 9800, 1),
            (users[1], 9400, 2),
            (users[2], 9050, 3),
            (users[0], 8900, 4),
        ]
        for row in leaderboard_rows:
            LeaderboardEntry.objects.create(user=row[0], score=row[1], rank=row[2])

        workout_rows = [
            (users[0], 'Spider Endurance Circuit', 'high', date.today() + timedelta(days=1), False),
            (users[1], 'Arc Reactor Core Blast', 'high', date.today() + timedelta(days=2), False),
            (users[2], 'Gotham Mobility Session', 'medium', date.today() + timedelta(days=1), True),
            (users[3], 'Themyscira Power Lift', 'high', date.today() + timedelta(days=3), False),
        ]
        for row in workout_rows:
            Workout.objects.create(
                user=row[0],
                title=row[1],
                intensity=row[2],
                scheduled_for=row[3],
                completed=row[4],
            )

        self.stdout.write(self.style.SUCCESS('테스트 데이터 적재를 완료했습니다.'))
