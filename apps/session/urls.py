from django.urls import path

from apps.session import views

app_name = "session"

urlpatterns = [
    path("", views.session_example_view, name="index"),
    path("all-sessions/", views.AllSessionsView.as_view(), name="all_sessions"),
    path(
        "current_session/", views.CurrentSessionViews.as_view(), name="current_sessions"
    ),
    path("current_session/", views.CurrentUserViews.as_view(), name="current_user"),
]
