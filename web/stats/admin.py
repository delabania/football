from django.contrib import admin
from .models import Player, Game, Stats

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass

@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    pass

