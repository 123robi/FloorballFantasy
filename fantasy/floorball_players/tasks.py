import re

from bs4 import BeautifulSoup
import requests

from celery import shared_task

from fantasy.common.enums import Enum
from fantasy.floorball_players.models import FloorballPlayer
from fantasy.floorball_teams.models import FloorballTeam


@shared_task
def get_players():
    for floorball_team in FloorballTeam.objects.all():
        request = requests.get(f'{floorball_team.team_url}{Enum.PLAYERS_URL}')
        soup = BeautifulSoup(request.content, 'html.parser')
        players = soup.find('div', {'id': re.compile(r'^PlayerStatsData')}).find('tbody').find_all('tr')

        for player in players:
            data = player.find_all('td')
            player_name = data[1].text
            games_played = data[4].text
            goals = data[5].text
            assists = data[8].text
            points = data[9].text
            penalties = data[10].text
            plus_minus = data[13].text

            try:
                player = FloorballPlayer.objects.get(name=player_name)
                player.games_played = games_played
                player.goals = goals
                player.assists = assists
                player.points = points
                player.penalties = penalties
                player.plus_minus = plus_minus
                player.team = floorball_team
                player.save()
            except FloorballPlayer.DoesNotExist:
                team = FloorballPlayer(
                    name=player_name, games_played=games_played, goals=goals,
                    assists=assists, points=points, penalties=penalties, plus_minus=plus_minus, team=floorball_team
                )
                team.save()
    return 'DONE'
