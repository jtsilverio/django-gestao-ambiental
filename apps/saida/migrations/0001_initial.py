# Generated by Django 4.2 on 2023-09-17 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("classe", "0001_initial"),
        ("destinacao", "0001_initial"),
        ("fornecedor", "0001_initial"),
        ("localidade", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Saida",
            fields=[
                ("id_saida", models.AutoField(primary_key=True, serialize=False)),
                ("data", models.DateField()),
                (
                    "peso",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "receita",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0, max_digits=10
                    ),
                ),
                (
                    "custo",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0, max_digits=10
                    ),
                ),
                ("n_evidencia", models.CharField(max_length=50)),
                ("cdf", models.CharField(blank=True, default="", max_length=50)),
                (
                    "id_classe",
                    models.ForeignKey(
                        db_column="id_classe",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="classe.classe",
                    ),
                ),
                (
                    "id_destinacao",
                    models.ForeignKey(
                        db_column="id_destinacao",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="destinacao.destinacao",
                    ),
                ),
                (
                    "id_fornecedor",
                    models.ForeignKey(
                        db_column="id_fornecedor",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="fornecedor.fornecedor",
                    ),
                ),
                (
                    "id_localidade",
                    models.ForeignKey(
                        db_column="id_localidade",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="localidade.localidade",
                    ),
                ),
            ],
            options={
                "verbose_name": "Saída",
                "verbose_name_plural": "Saídas",
                "db_table": "saida",
                "ordering": ["-id_saida"],
            },
        ),
    ]
