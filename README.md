celery -A config worker -l INFO -> to run celery localy

#Prices

##GoalKeeper price

Initial price is determined by the following formula:
price = (goals_conceded/games * (1 - wins/games)) * 100000 + 20000 * no_goals_conceded
if price is 0:
    price = 100000
else:
    max([100000, (300000 - price)])

https://www.ceskyflorbal.cz/osoba/0609050641 -> Jan baudisch is player not goalkeeper

insert into floorball_players_floorballplayer(name, games_played, points, goals, assists, penalties, plus_minus, floorball_team_id, new_price, old_price, player_url) values ('Jan Baudisch', 2, 1, 1, 0, 2, -5, 36, 100000, 100000, 'https://www.ceskyflorbal.cz/osoba/0609050641')