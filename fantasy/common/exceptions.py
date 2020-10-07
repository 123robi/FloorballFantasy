from rest_framework.exceptions import APIException


class UserAlreadyHasTeam(APIException):
    status_code = 400
    default_detail = 'User already has a team.'
    default_code = 'user_already_has_team'


class TeamSizeException(APIException):
    status_code = 400
    default_detail = 'You have to choose exactly 5 players.'
    default_code = 'time_size_exception'


class BudgetException(APIException):
    status_code = 400
    default_detail = 'You must not exceed the budget of 1000000.'
    default_code = 'budget_exceeded'
