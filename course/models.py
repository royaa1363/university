from django.db import models


class Main_unit(models.Model):
    name = models.CharField(max_length=256)
    unit_value = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Public_unit(models.Model):
    name = models.CharField(max_length=256)
    unit_value = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Major(models.Model):
    name = models.CharField(max_length=256)
    main_units = models.ManyToManyField(Main_unit)
    public_units = models.ManyToManyField(Public_unit)

    def __str__(self):
        return f'{self.name}'


class Student(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name} {self.first_name}- {self.major}"


class Term(models.Model):
    title = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f'{self.title}'


class Session(models.Model):
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return f'{self.major}-{self.term}'


class Teacher(models.Model):
    last_name = models.CharField(max_length=256)
    unit = models.ManyToManyField(Main_unit)

    def __str__(self):
        return f'{self.last_name}'
