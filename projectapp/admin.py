
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person, Person_detail

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email', 'location')

@admin.register(Person_detail)
class Person_detailAdmin(ImportExportModelAdmin):
    list_display = ('address', 'birth_date', 'phoneno')
# Register your models here.
