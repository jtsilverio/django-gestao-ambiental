from django.db import models


# Create your models here.
class Fugitivas(models.Model):
    id = models.AutoField(primary_key=True)
    tp_gas = models.CharField(max_length=50, blank=False, null=False)
    n_unidades = models.IntegerField(blank=False, null=False)
    recarga = models.BooleanField(blank=False, null=False)
    capacidade = models.IntegerField(blank=False, null=False)
    # data?

    def __str__(self):
        return f"{self.tp_gas}"

    class Meta:
        db_table = "fugitivas"
        verbose_name = "Fugitivas"
        verbose_name_plural = "Fugitivas"
        ordering = ["id"]
