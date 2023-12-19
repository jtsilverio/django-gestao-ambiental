# Generated by Django 4.2 on 2023-12-19 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("unidade_consumo", "0001_initial"),
        ("cluster", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Agua",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("data", models.DateField()),
                (
                    "fonte",
                    models.CharField(
                        choices=[
                            ("LM", "Ligação Municipal"),
                            ("P", "Poço"),
                            ("CS", "Captação Superfície"),
                            ("CP", "Caminhão Pipa"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "consumo",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "id_cluster",
                    models.ForeignKey(
                        db_column="id_cluster",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="cluster.cluster",
                    ),
                ),
                (
                    "id_unidade_consumo",
                    models.ForeignKey(
                        db_column="id_unidade_consumo",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="unidade_consumo.unidadeconsumo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Consumo de água",
                "verbose_name_plural": "Consumo de água",
                "db_table": "agua",
                "ordering": ["-id"],
            },
        ),
    ]
