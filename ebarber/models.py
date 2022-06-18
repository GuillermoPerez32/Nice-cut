from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Barber(models.Model):

    

    class Meta:
        verbose_name = _("Barber")
        verbose_name_plural = _("Barbers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Barber_detail", kwargs={"pk": self.pk})
