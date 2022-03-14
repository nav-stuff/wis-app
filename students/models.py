from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    program = models.ForeignKey('programs.Program', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.TextField()
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{} | {} | {}".format(self.student.name, self.subject, self.score)

class ParentsInfo(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    father_name = models.TextField()
    mother_name = models.TextField()

    def __str__(self):
        return "{} | {} | {}".format(self.student.name, self.father_name, self.mother_name)

class TutionFee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{} | {} ".format(self.student.name, self.amount)
