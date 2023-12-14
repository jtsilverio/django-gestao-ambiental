# Generated by Django 4.2 on 2023-12-14 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cluster", "0001_initial"),
        ("tipo_residuos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entrada",
            fields=[
                ("id_entrada", models.AutoField(primary_key=True, serialize=False)),
                ("data", models.DateField()),
                (
                    "peso",
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
                    "id_tp_residuos",
                    models.ForeignKey(
                        db_column="id_tp_residuos",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="tipo_residuos.tiporesiduos",
                    ),
                ),
            ],
            options={
                "db_table": "entrada",
                "ordering": ["-id_entrada"],
            },
        ),
    ]
