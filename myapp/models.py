from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    details = models.TextField()

    def __str__(self):
        return self.name


class Student(Person):
    college = models.CharField(max_length=255)
    age = models.IntegerField()
    def __str__(self):
        return self.name


class Parents(Person):
    related_to = models.ForeignKey(Student, on_delete=models.CASCADE,
     related_name="student_related_to")

    relationship = models.CharField(max_length=255, help_text="Father, Mother or any other relation")

    def __str__(self):
        return self.name