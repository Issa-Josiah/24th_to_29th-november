from django.db import models

# Create your models here.
class raws(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    purchase_Date = models.DateField()

    def __str__(self):
        return self.name

class fruit(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField()
    price = models.FloatField()
    date = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f" {self.name}   \n Price Tag:{self.price} \n Date goods bought:   {self.date}"