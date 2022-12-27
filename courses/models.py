from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Mentor(models.Model):
    name = models.CharField(max_length=30)
    experience = models.IntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    duration = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

