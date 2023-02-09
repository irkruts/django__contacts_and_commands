from django.urls import path

from apps.contacts import views
from apps.contacts.views import logout_user

app_name = "contacts"

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="index"),
    # path("", views.show_all_contacts, name="index"),
    path("edit_contact/", views.show_all_to_edit, name="show_to_edit"),
    # path("edit_contact/<int:pk>", views.edit_contact, name="edit"),
    path("edit_contact/<int:pk>", views.ContactUpdateView.as_view(), name="edit"),
    # path("create_contact/", views.create_contact, name="create"),
    path("create_contact/", views.ContactCreateView.as_view(), name="create"),
    path("delete_contact/", views.show_all_to_delete, name="show_to_delete"),
    # path("delete_contact/", views.ContactDeleteView.as_view(), name="show_to_delete"),
    path("delete_contact/<int:pk>/", views.ContactDeleteView.as_view(), name="delete"),
    path("register/", views.RegisterUserForm.as_view(), name="register"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
]
