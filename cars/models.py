from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    title= models.CharField(max_length = 50)
    price = models.IntegerField(blank=True, null=True)
    content =  models.TextField()
    image = models.ImageField(upload_to='cars/media/uploads/', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) # one to many relations between cars and brands
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='owned_cars')
    purchased = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1, blank=True, null=True)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.name}"