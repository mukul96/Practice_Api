from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=250,primary_key=True);
    address=models.CharField(max_length=250);
    gender=models.CharField(max_length=250);
    #id=models.IntegerField(auto_created=True)




