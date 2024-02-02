# Generated by Django 4.2 on 2024-02-02 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cluster", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UnidadeConsumo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=20)),
                (
                    "id_cluster",
                    models.ForeignKey(
                        db_column="id_cluster",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="cluster.cluster",
                    ),
                ),
            ],
            options={
                "verbose_name": "Unidade de Consumo",
                "verbose_name_plural": "Unidades de Consumo",
                "db_table": "unidade_consumo",
                "ordering": ["-id"],
            },
        ),
    ]
