from django.db import models

from apps.cidades.estados_brasileiros import ESTADOS_BRASILEIROS
from apps.cidades.models import Cidades
from apps.destinacao.models import Destinacao


class Fornecedor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(
        max_length=2, null=False, blank=False, choices=ESTADOS_BRASILEIROS
    )
    id_cidade = models.ForeignKey(
        Cidades,
        on_delete=models.PROTECT,
        related_name="fornecedor",
        blank=False,
    )
    destinacao = models.ManyToManyField(
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
