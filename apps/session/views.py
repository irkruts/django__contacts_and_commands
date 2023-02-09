import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

KEY__COUNT_OF_VISITS = "count_of_visits"


def session_example_view(request: WSGIRequest | HttpRequest) -> HttpResponse:
    session = request.session
    count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)
    visits_time = session.get("visits_time", datetime.datetime.now())
    count_of_visits += 1
    session[KEY__COUNT_OF_VISITS] = count_of_visits

    return render(
        request,
        "session/index.html",
        {
            "session_id": session.session_key,
            "count_of_visits": count_of_visits,
            "visits_time": visits_time,
            "title": "Session example",
        },
    )
