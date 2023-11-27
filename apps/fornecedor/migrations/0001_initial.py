# Generated by Django 4.2 on 2023-11-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("destinacao", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fornecedor",
            fields=[
                ("id_fornecedor", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=50)),
                (
                    "destinacao",
                    models.ManyToManyField(
                        blank=True,
                        db_table="fornecedor_destinacao",
                        related_name="fornecedor",
                        to="destinacao.destinacao",
                    ),
                ),
            ],
            options={
                "verbose_name": "Fornecedor",
                "verbose_name_plural": "Fornecedores",
                "db_table": "fornecedor",
                "ordering": ["nome"],
            },
        ),
    ]
