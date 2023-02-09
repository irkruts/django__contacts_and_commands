from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Contacts


class ArticleListView(ListView):
    model = Contacts


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contacts
    fields = (
        "id",
        "name",
        "date_of_birth",
        "avatar",
    )
    template_name_suffix = "_update_form"


class ContactCreateView(CreateView):
    model = Contacts
    fields = (
        "name",
        "phone",
        "date_of_birth",
        "avatar",
    )

    def get_success_url(self):
        return reverse_lazy("contacts:create")


# class ContactDeleteView(LoginRequiredMixin, DeleteView):


class ContactDeleteView(DeleteView):
    model = Contacts

    def get_success_url(self):
        return reverse_lazy("contacts:delete", kwargs={"pk": self.object.pk})


@login_required(login_url="contacts:login")
def show_all_to_edit(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request, "contacts/edit.html", {"title": "Contacts", "contacts": contacts}
    )


@login_required(login_url="contacts:login")
def show_all_to_delete(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request, "contacts/delete.html", {"title": "Contacts", "contacts": contacts}
    )


# def delete_contact(request: HttpRequest, pk) -> HttpResponse:
# contact = Contacts.objects.get(pk=pk)
# form = ContactsForm(instance=contact)
# contact.delete()
# return render(
# request,
# "contacts/contacts_confirm_delete.html",
# {"title": "Delete contact", "form": form, "contact": contact},
# )


class RegisterUserForm(CreateView):
    form_class = UserCreationForm
    template_name = "contacts/register.html"
    success_url = reverse_lazy("contacts:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("contacts:index")


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "contacts/login.html"

    # def get_success_url(self):
    #     return reverse_lazy("base:index")


def logout_user(request):
    logout(request)
    return redirect("/")
