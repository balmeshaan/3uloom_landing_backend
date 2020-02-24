from django.db import models

# Create your models here.
class Tutor(models.Model):
	name = models.CharField(max_length=105)
	subject = models.CharField(max_length=105)
	level = models.CharField(max_length=105)
	email = models.EmailField(max_length=105)

	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=105)
	email = models.EmailField(max_length=105)

	def __str__(self):
		return self.name