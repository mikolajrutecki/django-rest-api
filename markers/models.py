from django.db import models

# Create your models here.
class Marker(models.Model):
    created = models.DateTimeField(verbose_name="Data utworzenia", auto_now_add=True)
    phone = models.DecimalField(verbose_name="Numer telefonu", max_digits=9, decimal_places=0, null=True, blank=True)
    latitude = models.DecimalField(verbose_name="Szerokość", max_digits=9, decimal_places=6)
    longitude = models.DecimalField(verbose_name="Długość", max_digits=9, decimal_places=6)
    message = models.TextField(verbose_name="Wiadomość", null=True, blank=True)
    picture = models.TextField(verbose_name="Zdjęcie(base64)", null=True, blank=True)

    class Meta:
        verbose_name="Marker"
        verbose_name_plural="Markery"
        ordering = ('created',)
