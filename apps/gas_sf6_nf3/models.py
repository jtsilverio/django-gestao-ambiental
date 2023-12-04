from django.db import models

from apps.cluster.models import Cluster


class GasSF6NF3(models.Model):
    TIPO_GAS_CHOICES = [
        ("SF6", "SF6"),
        ("NF3", "NF3"),
    ]
    TIPO_CADASTRO_CHOICES = [
        ("Inicio", "Estoque Anual Inicial"),
        ("Final", "Estoque Anual Final"),
        ("Compra", "Compra de Gás"),
    ]

    id = models.AutoField(primary_key=True)
    data = models.DateField(blank=False, null=False)
    id_cluster = models.ForeignKey(
        Cluster, on_delete=models.PROTECT, blank=False, null=False
    )
    tp_gas = models.CharField(
        max_length=10, blank=False, null=False, choices=TIPO_GAS_CHOICES, default="SF6"
    )
    tp_cadastro = models.CharField(
        max_length=10, blank=False, null=False, choices=TIPO_CADASTRO_CHOICES
    )
    quantidade = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return f"{self.tp_gas}"

    class Meta:
        db_table = "gas_sf6_nf3"
        verbose_name = "Controle de Gás SF6 e NF3"
        verbose_name_plural = "Controle de Gases SF6 e NF3"
        ordering = ["-id"]
