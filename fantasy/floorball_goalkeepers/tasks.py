import re

from bs4 import BeautifulSoup
import requests

from celery import shared_task

from fantasy.common.enums import Enum
from fantasy.floorball_goalkeepers.models import Goalkeeper
from fantasy.floorball_players.models import FloorballPlayer
from fantasy.floorball_teams.models import FloorballTeam


@shared_task
def get_goalies():
    for floorball_team in FloorballTeam.objects.all():
        request = requests.get(f'{floorball_team.team_url}{Enum.GOALKEEPERS_URL}')
        soup = BeautifulSoup(request.content, 'html.parser')
        goalies = soup.find('div', {'id': re.compile(r'^GoalieStatsData')}).find('tbody').find_all('tr')

        for goalie in goalies:
            data = goalie.find_all('td')
            goalie_name = data[1].text
            games_played = data[4].text
            goals_conceded = data[7].text
            no_goals_conceded = data[8].text
            shoots_on_goal = data[9].text

            try:
                FloorballPlayer.objects.filter(name=goalie_name, floorball_team=floorball_team.id).delete()
                goalie = Goalkeeper.objects.get(name=goalie_name)
                goalie.games_played = games_played
                goalie.goals_conceded = goals_conceded
                goalie.no_goals_conceded = no_goals_conceded
                goalie.shoots_on_goal = shoots_on_goal
                goalie.save()
            except Goalkeeper.DoesNotExist:
                goalie = Goalkeeper(
                    name=goalie_name, games_played=games_played, goals_conceded=goals_conceded,
                    no_goals_conceded=no_goals_conceded, shoots_on_goal=shoots_on_goal, floorball_team=floorball_team
                )
                goalie.save()
    return 'DONE'
