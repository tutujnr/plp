from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=5)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
