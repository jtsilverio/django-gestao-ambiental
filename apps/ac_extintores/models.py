from django.db import models

from apps.cluster.models import Cluster


# Create your models here.
class ACExtintores(models.Model):
    TIPO_GAS_CHOICES = [
        ("CO2", "CO2"),
        ("CH4", "CH4"),
        ("N2O", "N2)"),
        ("R22", "R-22"),
        ("R410A", "R410-A"),
        ("OUT", "Outros"),
    ]

    FONTE_EMISSAO_CHOICES = [
        ("AC", "Ar Condicionado"),
        ("EXT", "Extintores"),
        ("TRA", "Transformadores"),
        ("OUT", "Outros"),
    ]

    TP_CADASTRO_CHOICES = [
        ("N", "NOVA UNIDADE"),
        ("R", "RECARGA"),
        ("D", "DISPENSA"),
    ]

    id = models.AutoField(primary_key=True)
    data = models.DateField(blank=False, null=False)
    id_cluster = models.ForeignKey(
        Cluster, on_delete=models.PROTECT, blank=False, null=False
    )
    fonte_emissao = models.CharField(
        max_length=3, blank=False, null=False, choices=FONTE_EMISSAO_CHOICES
    )
    tp_gas = models.CharField(
        max_length=5, blank=False, null=False, choices=TIPO_GAS_CHOICES
    )
    n_unidades = models.IntegerField(blank=False, null=False)
    tp_cadastro = models.CharField(
        max_length=3, blank=False, null=False, choices=TP_CADASTRO_CHOICES
    )
    carga = models.IntegerField(blank=True, null=False, default=0)
    capacidade = models.IntegerField(blank=True, null=False, default=0)
    recuperacao = models.IntegerField(blank=True, null=False, default=0)

    def __str__(self):
        return f"{self.tp_gas}"

    class Meta:
        db_table = "ac_extintores"
        verbose_name = "Ar Condicionado e Extintores"
        verbose_name_plural = "Ar Condicionado e Extintores"
        ordering = ["-id"]
