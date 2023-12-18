from django.db import models

from apps.cluster.models import Cluster
from apps.destinacao.models import Destinacao
from apps.fornecedor.models import Fornecedor
from apps.tipo_residuos.models import TipoResiduos


# Create your models here.
class Saida(models.Model):
    id_saida = models.AutoField(primary_key=True)
    data = models.DateField(null=False, blank=False)
    id_cluster = models.ForeignKey(Cluster, models.DO_NOTHING, db_column="id_cluster")
    id_tp_residuos = models.ForeignKey(
        TipoResiduos, models.DO_NOTHING, db_column="id_tp_residuos"
    )
    peso = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False, blank=False
    )
    id_fornecedor_destinacao = models.ForeignKey(
        Fornecedor,
        models.DO_NOTHING,
        db_column="id_fornecedor_destinacao",
        related_name="fornecedor_destinacao",
    )
    id_destinacao = models.ForeignKey(
        Destinacao, models.DO_NOTHING, db_column="id_destinacao"
    )
    id_fornecedor_transporte = models.ForeignKey(
        Fornecedor,
        models.DO_NOTHING,
        db_column="id_fornecedor_transporte",
        related_name="fornecedor_transporte",
    )
    receita = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False, blank=True
    )
    custo = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False, blank=True
    )
    n_evidencia = models.CharField(max_length=50)
    cdf = models.CharField(
        max_length=50,
        blank=True,
        default="",
    )

    def __str__(self):
        return f"ID:{self.id_saida}"

    class Meta:
        db_table = "saida"
        verbose_name = "Saída"
        verbose_name_plural = "Saídas"
        ordering = ["-id_saida"]
