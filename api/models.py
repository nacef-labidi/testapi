from django.db import models

class Bar(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    tel = models.CharField(max_length=30)
    email = models.EmailField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name
