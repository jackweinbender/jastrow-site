from django.db import models

# Create your models here.

class Page(models.Model):
    number = models.IntegerField()
    headword = models.TextField()

class Section(models.Model):
    title = models.TextField()

class Letter(models.Model):
    language = models.TextField()
    char = models.TextField()
    translit = models.TextField()
    ascii_translit = models.TextField()
    name = models.TextField()
    sort = models.IntegerField()