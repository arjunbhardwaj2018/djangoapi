from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.title