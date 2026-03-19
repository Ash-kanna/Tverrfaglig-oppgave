from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


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


from django.conf import settings


class Aktivitet(models.Model):
    navn = models.CharField(max_length=150)
    beskrivelse = models.TextField(blank=True)
    dato = models.DateTimeField()
    deltakere = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='aktiviteter')

    def __str__(self):
        return f"{self.navn} ({self.dato})"

    @property
    def antall_deltakere(self):
        return self.deltakere.count()