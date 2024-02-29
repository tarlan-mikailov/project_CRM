from django.db import models
# Create your models here.


class Resource(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Service(models.Model):
    name = models.CharField(max_length=50)
    resources = models.ManyToManyField(Resource)

    def __str__(self):
        return f'{self.name}'
