# Generated by Django 4.2 on 2023-05-19 11:59

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
                    "id_destinacao",
                    models.ManyToManyField(
                        db_table="fornecedor_destinacao",
                        related_name="destinacao",
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
