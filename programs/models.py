from django.db import models

class Program(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Lecturer(models.Model):
    name = models.TextField()
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name