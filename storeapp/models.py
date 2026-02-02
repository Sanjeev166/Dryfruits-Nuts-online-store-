from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    Age = models.IntegerField(default=0)

class Items(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    itemsimage = models.ImageField(upload_to='static/assets/images/')
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ForeignKey(Items, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)  
    
    def __str__(self):
        return self.user.username     
    

class Order(models.Model): 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_quantity = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    totalprice = models.FloatField(blank=True)  
    
    def __str__(self):
        return self.user.username  

