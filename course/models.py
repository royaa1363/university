from django.db import models


class University(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    university = models.ForeignKey(University, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
