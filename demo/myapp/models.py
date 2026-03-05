from django.db import models


class Bruker(models.Model):
    navn = models.CharField(max_length=100)
    epost = models.EmailField()

    def __str__(self):
        return self.navn


class Produkt(models.Model):
    navn = models.CharField(max_length=100)
    pris = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.navn


class Bestilling(models.Model):
    bruker = models.ForeignKey(Bruker, on_delete=models.CASCADE)
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    dato = models.DateField()

    def __str__(self):
        return f"{self.bruker} - {self.produkt}"