from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    semester = models.IntegerField(default=1)
    email = models.EmailField(unique=True)
    enrolled_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.roll_number} - {self.full_name}"