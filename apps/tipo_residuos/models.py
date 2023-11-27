from django.db import models


class TipoResiduos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, null=False, blank=False)
    classe = models.CharField(max_length=20, null=False, blank=False)
    unidade_medida = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        db_table = "tipo_residuos"
        verbose_name = "Tipo de Resíduo"
        verbose_name_plural = "Tipos de Resíduos"
        ordering = ["nome", "classe"]
