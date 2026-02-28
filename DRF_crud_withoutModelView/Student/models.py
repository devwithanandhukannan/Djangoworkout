from django.db import models

class Student(models.Model):
    name = models.CharField()
    age = models.PositiveBigIntegerField()
    mob = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name