from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Contacts
from .forms import ContactsForm, UserForm


def show_all_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request, "contacts/index.html", {"title": "Contacts", "contacts": contacts}
    )


def show_all_to_edit(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request, "contacts/edit.html", {"title": "Contacts", "contacts": contacts}
    )


def edit_contact(request: HttpRequest, pk: int) -> HttpResponse:
    contact = Contacts.objects.get(pk=pk)
    form = ContactsForm(instance=contact)
    return render(
        request, "contacts/edit_form.html", {"title": "Edit contact", "form": form}
    )


# https://www.youtube.com/watch?v=EX6Tt-ZW0so
def create_contact(request: HttpRequest) -> HttpResponse:
    form = UserForm()
    if request.method == "POST":
        # print("Printing POST:", request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "contacts/create.html", context)


def show_all_to_delete(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request, "contacts/delete.html", {"title": "Contacts", "contacts": contacts}
    )


def delete_contact(request: HttpRequest, pk) -> HttpResponse:
    contact = Contacts.objects.get(pk=pk)
    form = ContactsForm(instance=contact)
    contact.delete()
    # context = {'contact': contact}
    return render(
        request,
        "contact/delete_form.html",
        {"title": "Delete contact", "form": form, "contact": contact},
    )
