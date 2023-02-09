import datetime
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from apps.session.models import UserDataRequest


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


# class ArticleListView(ListView):
#     model = UserDataRequest
#     template_name = 'session/new.html'
#
# log = logging.getLogger('urllib3')  # works
#
# log.setLevel(logging.DEBUG)  # needed
# fh = logging.FileHandler("requests.log")
# log.addHandler(fh)
#
# requests.get('http://127.0.0.1:8000')


class AllSessionsView(ListView):
    model = UserDataRequest
    template_name = "session/middleware_info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All session info"
        visitor = UserDataRequest.objects.all()
        context["object_list"] = visitor
        return context


class CurrentSessionViews(ListView):
    model = UserDataRequest
    template_name = "session/current_session.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Current session"

        visitor = UserDataRequest.objects.filter(
            session_key=self.kwargs["session_key"]
        )  # some mistake

        context["object_list"] = visitor
        return context


class CurrentUserViews(ListView):
    model = UserDataRequest
    template_name = "session/current_user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Current user session info"

        visitor = UserDataRequest.objects.filter(user=self.kwargs["pk"])

        context["object_list"] = visitor
        return context
