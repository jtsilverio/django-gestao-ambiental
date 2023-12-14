from django.db import models

from apps.cidades.estados_brasileiros import ESTADOS_BRASILEIROS
from apps.cidades.models import Cidades


# Create your models here.
class Cluster(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=25, blank=False, null=False)
    estado = models.CharField(
        max_length=2,
        blank=False,
        null=False,
        choices=ESTADOS_BRASILEIROS,
    )
    id_cidade = models.ForeignKey(
        Cidades,
        on_delete=models.PROTECT,
        related_name="cluster",
        blank=False,
    )

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        db_table = "cluster"
        verbose_name = "Cluster"
        verbose_name_plural = "Clusters"
        ordering = ["estado", "nome"]
