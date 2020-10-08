from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique= true)
    location = models.CharField(max_length=100, blank=True)

    def isExists(self):

        if Person.objects.filter(email = self.email):
            return True

        return False

class Person_detail(models.Model):
    address = models.CharField(max_length=50)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    birth_date = models.DateField()
    phoneno = models.IntegerField()


# Create your models here.
