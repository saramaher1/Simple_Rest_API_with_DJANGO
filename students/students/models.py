from django.db import models


class Student(models.Model):
    studentname = models.CharField(max_length=200)
    age = models.IntegerField()
    course = models.CharField(max_length=200)
    collage = models.CharField(max_length=200)

    def __str__(self):
        return self.studentname
