# Generated by Django 4.2 on 2024-01-04 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cluster", "0001_initial"),
        ("unidade_consumo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Eletricidade",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("data", models.DateField()),
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
                "verbose_name": "Eletricidade",
                "verbose_name_plural": "Eletricidades",
                "db_table": "eletricidade",
                "ordering": ["-id"],
            },
        ),
    ]
