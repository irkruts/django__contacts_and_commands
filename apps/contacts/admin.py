from django.contrib import admin


from .models import Contacts, Group

admin.site.register(Contacts)


class ContactsInline(admin.TabularInline):
    model = Contacts


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = (ContactsInline,)
