# Generated by Django 4.2 on 2023-12-12 00:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TipoResiduos",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=20)),
                (
                    "classe",
                    models.CharField(
                        choices=[("I", "I"), ("IIA", "IIA"), ("IIB", "IIB")],
                        max_length=10,
                    ),
                ),
                (
                    "unidade_medida",
                    models.CharField(
                        choices=[
                            ("Kg", "Kilograma (Kg)"),
                            ("t", "Tonelada (t)"),
                            ("m", "Metro (m)"),
                            ("m²", "Metro Quadrado (m²)"),
                            ("m³", "Metro Cúbico (m³)"),
                            ("L", "Litro (L)"),
                            ("UN", "Unidade (UN)"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
            options={
                "verbose_name": "Tipo de Resíduo",
                "verbose_name_plural": "Tipos de Resíduos",
                "db_table": "tipo_residuos",
                "ordering": ["-id"],
            },
        ),
    ]
