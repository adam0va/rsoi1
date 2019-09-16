from django.db import models

class Person(models.Model):
    name = models.CharField(max_length = 150, null = False)
    age = models.SmallIntegerField(null = False)

    def __str__(self):
    	return f'{self.name}, age: {self.age}'

# Create your models here.
