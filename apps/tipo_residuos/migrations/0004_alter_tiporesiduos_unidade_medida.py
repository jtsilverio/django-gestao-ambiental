# Generated by Django 4.2 on 2024-02-04 21:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tipo_residuos", "0003_alter_tiporesiduos_unidade_medida"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tiporesiduos",
            name="unidade_medida",
            field=models.CharField(
                choices=[
                    ("kg", "Kilograma (Kg)"),
                    ("m", "Metro (m)"),
                    ("m²", "Metro Quadrado (m²)"),
                    ("m³", "Metro Cúbico (m³)"),
                    ("L", "Litro (L)"),
                    ("UN", "Unidade (UN)"),
                ],
                max_length=3,
            ),
        ),
    ]