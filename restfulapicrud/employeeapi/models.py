from django.db import models

# Create your models here.

class Employee(models.Model):
    Performance = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    Caste = models.CharField(max_length=50)
    Coaching = models.CharField(max_length=50)
    time = models.IntegerField()
    Class_ten_education = models.CharField(max_length=50)
    twelve_education = models.CharField(max_length=50)
    medium = models.CharField(max_length=50)
    Class_X_Percentage = models.CharField(max_length=50)
    Class_XII_Percentage = models.CharField(max_length=50)
    Father_occupation = models.CharField(max_length=50)
    Mother_occupation = models.CharField(max_length=50)
    
    
    
    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE