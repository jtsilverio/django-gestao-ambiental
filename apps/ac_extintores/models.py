from django.db import models

from apps.cluster.models import Cluster


# Create your models here.
class ACExtintores(models.Model):
    TIPO_GAS_CHOICES = [
        ("C02", "C02"),
        ("CH4", "CH4"),
        ("N20", "N20"),
        ("R-22", "R-22"),
        ("R410-A", "R410-A"),
        ("OUTROS", "OUTROS"),
    ]

    FONTE_EMISSAO_CHOICES = [
        ("AR CONDICIONADO", "AR CONDICIONADO"),
        ("EXTINTOR", "EXTINTOR"),
        ("TRANSFORMADOR", "TRANSFORMADOR"),
        ("OUTROS", "OUTROS"),
    ]

    TP_UNIDADE_CHOICES = [
        ("NOVA UNIDADE", "NOVA UNIDADE"),
        ("RECARGA", "RECARGA"),
        ("DISPENSA", "DISPENSA"),
    ]

    id = models.AutoField(primary_key=True)
    id_cluster = models.ForeignKey(
        Cluster, on_delete=models.PROTECT, blank=False, null=False
    )
    fonte_emissao = models.CharField(
        max_length=15, blank=False, null=False, choices=FONTE_EMISSAO_CHOICES
    )
    tp_gas = models.CharField(
        max_length=15, blank=False, null=False, choices=TIPO_GAS_CHOICES
    )
    n_unidades = models.IntegerField(blank=False, null=False)
    tp_unidade = models.CharField(
        max_length=15, blank=False, null=False, choices=TP_UNIDADE_CHOICES
    )
    carga = models.IntegerField(blank=True, null=False, default=0)
    capacidade = models.IntegerField(blank=True, null=False, default=0)
    recuperacao = models.IntegerField(blank=True, null=False, default=0)

    # DIVIDIR EM EXTIÇÃO E AR CONDICIONADO + SF6 NF3
    # -----
    # CLUSTER
    # TP_GAS (SF6, NF3)
    # ESTOQUE DE GAS NO INICIO DO ANO
    # ESTOQUE DE GAS NO FINAL DO ANO
    # QUANTIDADE DE GAS COMPRADO NO ANO

    def __str__(self):
        return f"{self.tp_gas}"

    class Meta:
        db_table = "ac_extintores"
        verbose_name = "Ar Condicionado e Extintores"
        verbose_name_plural = "Ar Condicionado e Extintores"
        ordering = ["-id"]
