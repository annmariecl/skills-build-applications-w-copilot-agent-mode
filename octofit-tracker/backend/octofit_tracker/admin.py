from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Team, Activity, Workout, Leaderboard

admin.site.register(get_user_model())
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Workout)
admin.site.register(Leaderboard)
