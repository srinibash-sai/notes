from django.db import models

# Create your models here.
class Credentials(models.Model):
    id=models.AutoField(primary_key=True)
    UserName=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)