from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class signtbl(models.Model):
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    roll = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class admintbl(models.Model):
    admin_username = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)

    def __str__(self):
        return self.admin_username

