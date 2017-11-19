from django.db import models


# Contact model
class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    age = models.IntegerField(max_length=3)
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    job = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name
