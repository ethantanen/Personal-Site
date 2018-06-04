from django.db import models

# Create your models here.
class JavaProject(models.Model):
    name = models.CharField(max_length=40)
    file = models.FileField()

    def __str__(self):
        return name 
