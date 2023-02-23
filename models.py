from django.db import models

# Create your models here.
class Swiggy(models.Model):
    restaurant = models.CharField(max_length=30)
    food = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    cost = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.food 
        # + ", " + self.restaurant