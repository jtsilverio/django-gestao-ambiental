from django.db import models

from .estados_brasileiros import ESTADOS_BRASILEIROS


class Cidades(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=60)
    estado = models.CharField(max_length=2, choices=ESTADOS_BRASILEIROS)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "cidades"
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ["nome"]
