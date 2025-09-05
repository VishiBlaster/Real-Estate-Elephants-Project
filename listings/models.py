from django.db import models

# Create your models here.
class Listing(models.Model):
  title=models.CharField(max_length=200)
  price=models.CharField(max_length=50)
  location=models.CharField(max_length=100)
  description=models.TextField()
  image=models.ImageField(upload_to='images/')
  bedrooms=models.IntegerField()
  bathrooms=models.IntegerField()
  def __str__(self):
    return self.title