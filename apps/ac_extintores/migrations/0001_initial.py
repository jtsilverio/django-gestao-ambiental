# Generated by Django 4.2 on 2023-12-11 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cluster", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ACExtintores",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("data", models.DateField()),
                (
                    "fonte_emissao",
                    models.CharField(
                        choices=[
                            ("AC", "Ar Condicionado"),
                            ("EXT", "Extintores"),
                            ("TRA", "Transformadores"),
                            ("OUT", "Outros"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "tp_gas",
                    models.CharField(
                        choices=[
                            ("CO2", "CO2"),
                            ("CH4", "CH4"),
                            ("N2O", "N2)"),
                            ("R22", "R-22"),
                            ("R410A", "R410-A"),
                            ("OUT", "Outros"),
                        ],
                        max_length=5,
                    ),
                ),
                ("n_unidades", models.IntegerField()),
                (
                    "tp_cadastro",
                    models.CharField(
                        choices=[
                            ("N", "NOVA UNIDADE"),
                            ("R", "RECARGA"),
                            ("D", "DISPENSA"),
                        ],
                        max_length=3,
                    ),
                ),
                ("carga", models.IntegerField(blank=True, default=0)),
                ("capacidade", models.IntegerField(blank=True, default=0)),
                ("recuperacao", models.IntegerField(blank=True, default=0)),
                (
                    "id_cluster",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cluster.cluster",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ar Condicionado e Extintores",
                "verbose_name_plural": "Ar Condicionado e Extintores",
                "db_table": "ac_extintores",
                "ordering": ["-id"],
            },
        ),
    ]
