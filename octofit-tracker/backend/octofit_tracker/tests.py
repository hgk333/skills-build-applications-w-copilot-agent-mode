from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from .models import Activity, LeaderboardEntry, Team, UserProfile, Workout


class OctofitCollectionApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Marvel Team Test', universe='marvel')
        self.user = UserProfile.objects.create(
            name='Peter Parker Test',
            email='spiderman-test@octofit.com',
            team=self.team,
        )
        Activity.objects.create(
            user=self.user,
            activity_type='Web Swing Cardio',
            duration_minutes=30,
            calories_burned=250,
            performed_at=timezone.now() - timedelta(hours=1),
        )
        LeaderboardEntry.objects.create(user=self.user, score=5000, rank=1)
        Workout.objects.create(
            user=self.user,
            title='Spider Endurance Circuit',
            intensity='high',
            scheduled_for=timezone.now().date(),
            completed=False,
        )

    def test_api_root_contains_all_collection_links(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.json())
        self.assertIn('teams', response.json())
        self.assertIn('activities', response.json())
        self.assertIn('leaderboard', response.json())
        self.assertIn('workouts', response.json())

    def test_users_collection_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_teams_collection_endpoint(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_activities_collection_endpoint(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_leaderboard_collection_endpoint(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_workouts_collection_endpoint(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
