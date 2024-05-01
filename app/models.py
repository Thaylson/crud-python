from django.db import models

# Create your models here.
class Pessoa(models.Model):
    Nome = models.CharField(max_length=150)
    CPF = models.IntegerField()
    Email = models.EmailField(max_length=150)
