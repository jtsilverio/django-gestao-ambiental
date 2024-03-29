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
            name="GasSF6NF3",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("data", models.DateField()),
                (
                    "tp_gas",
                    models.CharField(
                        choices=[("SF6", "SF6"), ("NF3", "NF3")],
                        default="SF6",
                        max_length=10,
                    ),
                ),
                (
                    "tp_cadastro",
                    models.CharField(
                        choices=[
                            ("Inicio", "Estoque Anual Inicial"),
                            ("Final", "Estoque Anual Final"),
                            ("Compra", "Compra de Gás"),
                        ],
                        max_length=10,
                    ),
                ),
                ("quantidade", models.IntegerField(default=0)),
                (
                    "id_cluster",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cluster.cluster",
                    ),
                ),
            ],
            options={
                "verbose_name": "Controle de Gás SF6 e NF3",
                "verbose_name_plural": "Controle de Gases SF6 e NF3",
                "db_table": "gas_sf6_nf3",
                "ordering": ["-id"],
            },
        ),
    ]
