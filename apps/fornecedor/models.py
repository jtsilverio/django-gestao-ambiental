from django.db import models

from apps.cidades.estados_brasileiros import ESTADOS_BRASILEIROS
from apps.cidades.models import Cidades
from apps.destinacao.models import Destinacao

TP_FORNECEDOR_CHOICES = (
    ("Transporte", "Transporte de Resíduos"),
    ("Destinação Final", "Destinação Final de Resíduos"),
    ("Serviço de Terceiros", "Serviço de Terceiros"),
)


class TipoFornecedor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(
        max_length=25, null=False, blank=False, choices=TP_FORNECEDOR_CHOICES
    )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "tipo_fornecedor"
        ordering = ["id"]
        verbose_name = "Tipo de Fornecedor"
        verbose_name_plural = "Tipos de Fornecedores"


class Fornecedor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
    id_tp_fornecedor = models.ManyToManyField(
        TipoFornecedor,
        db_table="fornecedor_tp_fornecedor",
        related_name="fornecedor",
        blank=False,
    )
    estado = models.CharField(
        max_length=2, null=False, blank=False, choices=ESTADOS_BRASILEIROS
    )
    id_cidade = models.ForeignKey(
        Cidades,
        on_delete=models.PROTECT,
        related_name="fornecedor",
        blank=False,
    )
    id_destinacao = models.ManyToManyField(
        Destinacao,
        db_table="fornecedor_destinacao",
        related_name="fornecedor",
        blank=True,
    )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "fornecedor"
        ordering = ["nome"]
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
