from django.http import HttpResponse

from fantasy.floorball_players.tasks import get_players


def index(request):
    return HttpResponse(get_players())
