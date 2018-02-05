from django.db import models

# Create your models here.

class Page(models.Model):
    number = models.IntegerField(unique=True)
    headword = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return f"{self.number} - {self.headword}"

class Section(models.Model):
    title = models.CharField(max_length=256)
    sort_order = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.sort_order} - {self.title}"

class Letter(models.Model):
    language = models.CharField(max_length=256)
    char = models.CharField(max_length=256)
    translit = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    sort_order = models.IntegerField()
    def __str__(self):
        return f"{self.language}: {self.char} - {self.name}"