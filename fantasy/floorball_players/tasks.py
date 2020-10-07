import re

from bs4 import BeautifulSoup
import requests

from celery import shared_task

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from fantasy.common.enums import Enum
from fantasy.floorball_goalkeepers.tasks import get_goalies
from fantasy.floorball_players.models import FloorballPlayer
from fantasy.floorball_teams.models import FloorballTeam
from fantasy.selenium_driver.helpers import install_web_driver, find_element, wait_until
from selenium.webdriver.support import expected_conditions as EC


@shared_task()
def set_players_initial_price():
    driver = install_web_driver()
    for index, floorball_player in enumerate(FloorballPlayer.objects.all()):
        print(f'{index} of {FloorballPlayer.objects.all().count()}')
        print(f'URL: {floorball_player.player_url}')
        driver.get(floorball_player.player_url)
        select = Select(find_element(driver, By.ID, 'id_seasonID'))
        select.select_by_value('25')
        wait_until(
            driver,
            EC.visibility_of_element_located(
                (By.XPATH, '//h2[contains(text(), "Statistiky hráče v sezóně") and contains(text(), "2019/2020")]')
            )
        )
        rows = find_element(
            driver, By.XPATH, '//tbody[contains(@id, "PlayerStatsGrid")]'
        ).find_elements(By.TAG_NAME, 'tr')

        games, goals, assists, penalties = [0, 0, 0, 0]
        for tr in rows:
            if 'Superliga florbalu' in tr.text:
                if 'základní část' in tr.text or 'play-down' in tr.text or 'play-off':
                    data_cells = tr.find_elements(By.TAG_NAME, 'td')
                    games += int(data_cells[3].text)
                    goals += int(data_cells[4].text)
                    assists += int(data_cells[5].text)
                    penalties += int(data_cells[7].text)
        if games != 0:
            floorball_player.new_price = max(
                [100000, (100000 + (goals/games * 2 + assists/games - penalties/games * 0.5) * 120000)]
            )
            floorball_player.old_price = floorball_player.new_price
            floorball_player.save()
        else:
            floorball_player.new_price = 100000
            floorball_player.old_price = floorball_player.new_price
            floorball_player.save()


@shared_task
def get_players():
    for floorball_team in FloorballTeam.objects.all():
        request = requests.get(f'{floorball_team.team_url}{Enum.PLAYERS_URL}')
        soup = BeautifulSoup(request.content, 'html.parser')
        players = soup.find('div', {'id': re.compile(r'^PlayerStatsData')}).find('tbody').find_all('tr')

        for player in players:
            data = player.find_all('td')
            player_name = data[1].text
            player_url = f'{Enum.BASE_URL}{data[1].find("a")["href"]}'
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
                player.floorball_team = floorball_team
                player.player_url = player_url
                player.save()
            except FloorballPlayer.DoesNotExist:
                team = FloorballPlayer(
                    name=player_name, games_played=games_played, goals=goals,
                    assists=assists, points=points, penalties=penalties,
                    plus_minus=plus_minus, player_url=player_url, floorball_team=floorball_team
                )
                team.save()
    get_goalies()
    return 'DONE'
