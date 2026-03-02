from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    
class Bruker(models.Model):
    navn = models.CharField(max_length=100)
    epost = models.EmailField()

class Produkt(models.Model):
    navn = models.CharField(max_length=100)
    pris = models.DecimalField(max_digits=10, decimal_places=2)

class Bestilling(models.Model):
    bruker = models.ForeignKey(Bruker, on_delete=models.CASCADE)
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    dato = models.DateField()