# Generated by Django 4.2 on 2024-01-04 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tipo_combustivel", "0001_initial"),
        ("cluster", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Combustivel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("dt_combustivel", models.DateField()),
                (
                    "fonte",
                    models.CharField(
                        choices=[("Fixa", "Fonte Fixa"), ("Móvel", "Fonte Móvel")],
                        max_length=5,
                    ),
                ),
                (
                    "consumo",
                    models.DecimalField(decimal_places=3, default=0, max_digits=10),
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
                    "id_tp_combustivel",
                    models.ForeignKey(
                        db_column="id_tp_combustivel",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="tipo_combustivel.tipocombustivel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Combustível",
                "verbose_name_plural": "Combustíveis",
                "db_table": "combustivel",
                "ordering": ["-id"],
            },
        ),
    ]
