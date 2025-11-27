from django.db import models

# Create your models here.
class One(models.Model):
    Name = models.CharField(max_length=100)
    age = models.IntegerField()
    birth_year = models.DateField()
    message = models.TextField()
    def __str__(self):
        return self.Name

class Fruits(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField()
    price = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    # class Meta:
    #     ordering = ['-created_at, updated_at']
    def __str__(self):
        return self.name

