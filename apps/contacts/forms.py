from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import SelectDateWidget
from django.forms import ModelForm


from apps.contacts.models import Contacts


class UserForm(ModelForm):
    date = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Contacts
        fields = "__all__"


class ContactsForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Contacts
        fields = "__all__"


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput)
    first_name = forms.CharField(
        label="Firs name", widget=forms.TextInput, required=False
    )
    last_name = forms.CharField(
        label="Last name", widget=forms.TextInput, required=False
    )
    email = forms.EmailField(label="Email", widget=forms.EmailInput())
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput())
    avatar = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar",
            "password1",
            "password2",
        )
