from models import Game,GameStatistic,Statistic,Team,TeamGame
from tastypie.resources import ModelResource

class GameResource(ModelResource):
    class Meta:
        queryset = Game.objects.all()
        resource_name = 'game'
        
class GameStatisticResource(ModelResource):
    class Meta:
        queryset = GameStatistic.objects.all()
        resource_name = 'game-statistic'

class StatisticResource(ModelResource):
    class Meta:
        queryset = Statistic.objects.all()
        resource_name = 'statistic'

class TeamResource(ModelResource):
    class Meta:
        queryset = Team.objects.all()
        resource_name = 'team'

class TeamGameResource(ModelResource):
    class Meta:
        queryset = TeamGame.objects.all()
        resource_name = 'team-game'