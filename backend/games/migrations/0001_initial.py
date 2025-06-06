# Generated by Django 5.1.3 on 2025-03-26 09:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('registration', 'Registration Open'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='registration', max_length=20)),
                ('min_players', models.PositiveIntegerField(default=3)),
                ('max_players', models.PositiveIntegerField(default=5)),
                ('winning_score', models.PositiveIntegerField(default=10)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_tournaments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_player1', models.PositiveIntegerField(default=0)),
                ('score_player2', models.PositiveIntegerField(default=0)),
                ('winning_score', models.PositiveIntegerField(default=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('ready', 'Ready'), ('in_progress', 'In Progress'), ('interrupted', 'Interrupted'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='pending', max_length=20)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1_games', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2_games', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='won_games', to=settings.AUTH_USER_MODEL)),
                ('tournament', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches', to='games.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='TournamentPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=50)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='games.tournament')),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='won_tournament', to='games.tournamentplayer'),
        ),
    ]
