from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team='Marvel'),
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
            User(name='Batman', email='batman@dc.com', team='DC'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user='Spider-Man', type='Running', duration=30),
            Activity(user='Iron Man', type='Cycling', duration=45),
            Activity(user='Wonder Woman', type='Swimming', duration=60),
            Activity(user='Batman', type='Yoga', duration=20),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        leaderboard = [
            Leaderboard(user='Spider-Man', points=100),
            Leaderboard(user='Iron Man', points=90),
            Leaderboard(user='Wonder Woman', points=95),
            Leaderboard(user='Batman', points=85),
        ]
        for entry in leaderboard:
            entry.save()

        # Workouts
        workouts = [
            Workout(name='Cardio Blast', description='High intensity cardio workout.'),
            Workout(name='Strength Training', description='Full body strength exercises.'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
