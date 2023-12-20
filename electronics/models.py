from django.db import models
class product(models.Model):
    name=models.CharField(max_length=100)
    details=models.TextField()
    price=models.IntegerField()
    read=models.IntegerField()
    thumbnail=models.URLField()

# Create your models here.
