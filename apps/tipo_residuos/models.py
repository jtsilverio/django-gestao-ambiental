from django.db import models


class TipoResiduos(models.Model):
    UNIDADES_MEDIDA_CHOICES = [
        ("Kg", "Kilograma (Kg)"),
        ("t", "Tonelada (t)"),
        ("m", "Metro (m)"),
        ("m²", "Metro Quadrado (m²)"),
        ("m³", "Metro Cúbico (m³)"),
        ("L", "Litro (L)"),
        ("UN", "Unidade (UN)"),
    ]

    CLASSE_CHOICES = [
        ("I", "I"),
        ("IIA", "IIA"),
        ("IIB", "IIB"),
    ]

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, null=False, blank=False)
    classe = models.CharField(
        max_length=10, choices=CLASSE_CHOICES, null=False, blank=False
    )
    unidade_medida = models.CharField(
        max_length=2, choices=UNIDADES_MEDIDA_CHOICES, null=False, blank=False
    )

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        db_table = "tipo_residuos"
        verbose_name = "Tipo de Resíduo"
        verbose_name_plural = "Tipos de Resíduos"
        ordering = ["-id"]
