from django.db import models

from apps.cidades.estados_brasileiros import ESTADOS_BRASILEIROS


class Cidades(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=60)
    estado = models.CharField(max_length=2, choices=ESTADOS_BRASILEIROS)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "cidades"
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ["nome"]
