from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField
    isAvailable = models.BooleanField

    def __str__(self):
        return self.name
    
