from bs4 import BeautifulSoup
import requests

from celery import shared_task

from fantasy.floorball_teams.models import FloorballTeam

base_url = 'https://www.ceskyflorbal.cz'
teams_url = '/superliga-muzi/tabulka'


# it takes quite a lot of time to get the team url
def get_team_img_url(team_url):
    request = requests.get(team_url)
    soup = BeautifulSoup(request.content, 'html.parser')
    return soup.find('img', {'class': 'team-logo'})['src']


@shared_task
def get_teams():
    request = requests.get(f'{base_url}{teams_url}')
    soup = BeautifulSoup(request.content, 'html.parser')
    teams_table = soup.find('div', {'class': 'datagrid'}).find('table').find('tbody')
    rows = teams_table.find_all('tr')

    for row in rows:
        cells = row.find_all('td')
        team_name = cells[2].text
        team_url = f'{base_url}{cells[2].find("a")["href"]}'
        wins = cells[4].text
        wins_after_over_time = cells[5].text
        loses_after_over_time = cells[6].text
        loses = cells[7].text
        points = cells[8].text
        try:
            team = FloorballTeam.objects.get(name=team_name)
            team.wins = wins.strip()
            team.loses = loses.strip()
            team.wins_after_over_time = wins_after_over_time.strip()
            team.loses_after_over_time = loses_after_over_time.strip()
            team.points = points.strip()
            team.save()
        except FloorballTeam.DoesNotExist:
            team = FloorballTeam(
                name=team_name, wins=wins, loses=loses,
                wins_after_over_time=wins_after_over_time,
                loses_after_over_time=loses_after_over_time,
                points=points, image_url=f'{base_url}{get_team_img_url(team_url)}'
            )
            team.save()
    return 'DONE'
