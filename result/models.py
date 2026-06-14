from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    math = models.IntegerField()
    science = models.IntegerField()
    english = models.IntegerField()

    def percentage(self):
        return (self.math + self.science + self.english) / 3
