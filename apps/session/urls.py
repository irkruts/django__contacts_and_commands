from django.urls import path

from apps.session import views

app_name = "session"

urlpatterns = [
    path("", views.session_example_view, name="index"),
]
