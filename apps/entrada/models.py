from django.db import models

from apps.cluster.models import Cluster
from apps.tipo_residuos.models import TipoResiduos


class Entrada(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField(null=False, blank=False)
    id_tp_residuos = models.ForeignKey(
        TipoResiduos,
        models.DO_NOTHING,
        db_column="id_tp_residuos",
    )

    id_cluster = models.ForeignKey(
        Cluster,
        models.DO_NOTHING,
        db_column="id_cluster",
    )
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"ID:{self.id_entrada}"

    class Meta:
        db_table = "entrada"
        ordering = ["-id"]
