from django.db import models

from apps.cluster.models import Cluster


class Agua(models.Model):
    FONTE_CHOICES = [
        ("LM", "Ligação Municipal"),
        ("P", "Poço"),
        ("CS", "Captação Superfície"),
        ("CP", "Caminhão Pipa"),
    ]

    id = models.AutoField(primary_key=True)
    id_cluster = models.ForeignKey(
        Cluster,
        models.DO_NOTHING,
        db_column="id_cluster",
    )
    id_unidade_consumo = models.ForeignKey(
        "unidade_consumo.UnidadeConsumo",
        models.DO_NOTHING,
        db_column="id_unidade_consumo",
    )
    data = models.DateField(null=False, blank=False)
    fonte = models.CharField(
        max_length=3,
        choices=FONTE_CHOICES,
        null=False,
        blank=False,
    )
    consumo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"ID:{self.id}"

    class Meta:
        db_table = "agua"
        verbose_name = "Consumo de água"
        verbose_name_plural = "Consumo de água"
        ordering = ["-id"]
