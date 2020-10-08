from import_export import resources
from .models import Person, Person_detail

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person


class Person_detailResource(resources.ModelResource):
    class Meta:
        model = Person_detail