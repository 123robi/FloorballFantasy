from django.http import HttpResponse

from fantasy.floorball_teams.tasks import get_teams


def index(request):
    return HttpResponse(get_teams())
