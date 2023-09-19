from django.db import models


class University(models.Model):
    name = models.CharField(max_length=256)


class Student(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True)
    # university = models.CharField(max_length=256)