from models import Game,Team,GameStatistic,Statistic,TeamGame
from datetime import datetime 
def store_footbal_data(reader):
    teams = dict([(x.name,x) for x in Team.objects.all()])
    statistics = dict([(x.name,x) for x in Statistic.objects.all()])
    for row in reader:
        game_name = "%s at %s" % (row['HomeTeam'], row['AwayTeam'])
        game_datetime = datetime.strptime(row['Date'],"%d/%m/%y")
        game,created = Game.objects.get_or_create(name=game_name,start_date=game_datetime.date())
        if "Attendance" in row and row["Attendance"]:
            game.attendance = int(row["Attendance"]) 
        if "Referee" in row and row["Referee"]:
            game.referee = row["Referee"]
        game.save()
        
        t1_game,created = TeamGame.objects.get_or_create(
                    team=teams[row['HomeTeam']],
                    game = game,
                )
        t1_game.home_field=True
        t1_game.save()
        
        t2_game,created = TeamGame.objects.get_or_create(
                    team=teams[row['AwayTeam']],
                    game = game,
                )
        
        home_shots,created = GameStatistic.objects.get_or_create(
                team=teams[row['HomeTeam']],
                game=game,
                statistic = statistics['shots'],
                period=0,
                defaults={'value':int(row['HS'])}
                )
        away_shots,created = GameStatistic.objects.get_or_create(
                team=teams[row['AwayTeam']],
                game=game,
                statistic = statistics['shots'],
                period=0,
                defaults={'value':int(row['AS'])}
                )
        hst,created = GameStatistic.objects.get_or_create(
                team=teams[row['HomeTeam']],
                game=game,
                statistic = statistics['shots_on_target'],
                period=0,
                defaults={'value':int(row['HST'])}
                )
        ast,created = GameStatistic.objects.get_or_create(
                team=teams[row['AwayTeam']],
                game=game,
                statistic = statistics['shots_on_target'],
                period=0,
                defaults={'value':int(row['AST'])}
                )
        home_final_score,created = GameStatistic.objects.get_or_create(
                team=teams[row['HomeTeam']],
                game=game,
                statistic = statistics['goals'],
                period=0,
                defaults={'value':int(row['FTHG'])}
                )
        away_final_score,created = GameStatistic.objects.get_or_create(
                team=teams[row['AwayTeam']],
                game=game,
                statistic = statistics['goals'],
                period=0,
                defaults={'value':int(row['FTAG'])}
                )
        
        home_corners,created = GameStatistic.objects.get_or_create(
                team=teams[row['HomeTeam']],
                game=game,
                statistic = statistics['corners'],
                period=0,
                defaults={'value':int(row['HC'])}
                )
        away_corners,created = GameStatistic.objects.get_or_create(
                team=teams[row['AwayTeam']],
                game=game,
                statistic = statistics['corners'],
                period=0,
                defaults={'value':int(row['AC'])}
                )
        home_yellow_cards,created = GameStatistic.objects.get_or_create(
                team=teams[row['HomeTeam']],
                game=game,
                statistic = statistics['yellow_cards'],
                period=0,
                defaults={'value':int(row['HY'])}
                )
        away_yellow_cards,created = GameStatistic.objects.get_or_create(
                team=teams[row['AwayTeam']],
                game=game,
                statistic = statistics['yellow_cards'],
                period=0,
                defaults={'value':int(row['AY'])}
                )
        home_red_cards,created = GameStatistic.objects.get_or_create(
                team=teams[row['HomeTeam']],
                game=game,
                statistic = statistics['red_cards'],
                period=0,
                defaults={'value':int(row['HR'])}
                )
        away_red_cards,created = GameStatistic.objects.get_or_create(
                team=teams[row['AwayTeam']],
                game=game,
                statistic = statistics['red_cards'],
                period=0,
                defaults={'value':int(row['AR'])}
                )
        home_fouls,created = GameStatistic.objects.get_or_create(
                team=teams[row['HomeTeam']],
                game=game,
                statistic = statistics['fouls'],
                period=0,
                defaults={'value':int(row['HF'])}
                )
        away_fouls,created = GameStatistic.objects.get_or_create(
                team=teams[row['AwayTeam']],
                game=game,
                statistic = statistics['fouls'],
                period=0,
                defaults={'value':int(row['AF'])}
                ) 