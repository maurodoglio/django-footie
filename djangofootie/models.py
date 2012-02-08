from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=128)
    
class Game(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateField()
    attendance=models.PositiveIntegerField(blank=True,null=True)
    referee=models.CharField(blank=True, max_length=128)
    class Meta:
        unique_together=['name','start_date']

class Statistic(models.Model):
    name=models.CharField(max_length=128)
    
class TeamGame(models.Model):
    team=models.ForeignKey(Team)
    game=models.ForeignKey(Game)
    home_field=models.BooleanField(default=False)
    class Meta:
        unique_together=['team','game']
    
class GameStatistic(models.Model):
    team=models.ForeignKey(Team)
    game=models.ForeignKey(Game)
    statistic=models.ForeignKey(Statistic)
    period=models.PositiveSmallIntegerField(blank=True,null=True)
    value=models.PositiveSmallIntegerField()
    
    class Meta:
        unique_together=['team','game','statistic','period']