from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):
    date = models.DateTimeField()

    def __str__(self):
        return self.date.strftime("%Y-%m-%d %H:%M")


class Stats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    goals = models.IntegerField()
    assists = models.IntegerField()

    def __str__(self):
        return f"{self.game}: {self.player} -> ({self.goals}, {self.assists})"
