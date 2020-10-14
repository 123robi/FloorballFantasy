import re

from bs4 import BeautifulSoup
import requests

from celery import shared_task
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from fantasy.common.enums import Enum
from fantasy.floorball_goalkeepers.models import Goalkeeper
from fantasy.floorball_players.models import FloorballPlayer
from fantasy.floorball_teams.models import FloorballTeam
from fantasy.selenium_driver.helpers import install_web_driver, find_element, wait_until, get_parent
from selenium.webdriver.support import expected_conditions as EC


@shared_task()
def set_goalie_initial_price():
    driver = install_web_driver()
    for index, floorball_goalie in enumerate(Goalkeeper.objects.all()):
        print(f'{index} of {Goalkeeper.objects.all().count()}')
        print(f'URL: {floorball_goalie.goalie_url}')
        driver.get(floorball_goalie.goalie_url)
        try:
            select = Select(
                get_parent(find_element(driver, By.XPATH, '//div[contains(@id, "GoalieStatsGrid")]')
                           ).find_element(By.ID, 'id_seasonID'))
            select.select_by_value('25')
        except:  # noqa: E722
            print('This is not a goalkeeper!')
        wait_until(
            driver,
            EC.visibility_of_element_located(
                (By.XPATH, '//h2[contains(text(), "Statistiky brankáře v sezóně") and contains(text(), "2019/2020")]')
            )
        )
        rows = find_element(
            driver, By.XPATH, '//tbody[contains(@id, "GoalieStatsGrid")]'
        ).find_elements(By.TAG_NAME, 'tr')

        games, wins, goals_conceded, no_goals_conceded, time_in_goal = [0, 0, 0, 0, 0]
        for tr in rows:
            if 'Superliga florbalu' in tr.text:
                if 'základní část' in tr.text or 'play-down' in tr.text or 'play-off':
                    data_cells = tr.find_elements(By.TAG_NAME, 'td')
                    games += int(data_cells[3].text)
                    time_in_goal += int(float(data_cells[4].text))
                    wins += int(data_cells[5].text)
                    goals_conceded += int(data_cells[6].text)
                    no_goals_conceded += int(data_cells[7].text)
        if games != 0:
            price = time_in_goal * 200 + wins/games * 100000 - goals_conceded * 500 + no_goals_conceded * 50000
            floorball_goalie.new_price = max([price, 50000])
            floorball_goalie.old_price = floorball_goalie.new_price
            floorball_goalie.save()
        else:
            floorball_goalie.new_price = 50000
            floorball_goalie.old_price = floorball_goalie.new_price
            floorball_goalie.save()


@shared_task
def get_goalies():
    for floorball_team in FloorballTeam.objects.all():
        request = requests.get(f'{floorball_team.team_url}{Enum.GOALKEEPERS_URL}')
        soup = BeautifulSoup(request.content, 'html.parser')
        goalies = soup.find('div', {'id': re.compile(r'^GoalieStatsData')}).find('tbody').find_all('tr')

        for goalie in goalies:
            data = goalie.find_all('td')
            goalie_name = data[1].text
            goalie_url = f'{Enum.BASE_URL}{data[1].find("a")["href"]}'
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
                goalie.goalie_url = goalie_url
                goalie.save()
            except Goalkeeper.DoesNotExist:
                goalie = Goalkeeper(
                    name=goalie_name, games_played=games_played, goals_conceded=goals_conceded, goalie_url=goalie_url,
                    no_goals_conceded=no_goals_conceded, shoots_on_goal=shoots_on_goal, floorball_team=floorball_team
                )
                goalie.save()
    return 'DONE'
