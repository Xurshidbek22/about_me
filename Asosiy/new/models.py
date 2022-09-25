from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=255)
    sana = models.DateField()
    matn = models.CharField(max_length=255)
    rasm = models.FileField(max_length=255)
    def __str__(self):return self.sarlavha

class Intervyu(models.Model):
    sarlavha = models.CharField(max_length=255)
    sana = models.DateField()
    link = models.CharField(max_length=255)
    rasm = models.FileField(max_length=255)
    def __str__(self):return self.sarlavha

class About(models.Model):
    ism = models.CharField(max_length=255)
    tugilgan_yil = models.DateField()
    soha = models.CharField(max_length=255)
    viloyat = models.CharField(max_length=255)
    rasm = models.FileField(max_length=255)
    def __str__(self):return self.ism



# Create your models here.
