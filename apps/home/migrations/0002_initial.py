# Generated by Django 4.2 on 2024-01-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("home", "0001_create_database_views"),
    ]

    operations = [
        migrations.CreateModel(
            name="ResumoMensalResiduos",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("tipo", models.CharField(max_length=10)),
                ("ano", models.CharField(max_length=5)),
                ("mes", models.CharField(max_length=5)),
                ("cluster", models.CharField(max_length=50)),
                ("tp_residuos", models.CharField(max_length=50)),
                ("peso", models.FloatField()),
                ("receita", models.FloatField()),
                ("custo", models.FloatField()),
            ],
            options={
                "verbose_name_plural": "Resumo Mensal Resíduos",
                "db_table": "resumo_mensal_residuos",
                "managed": False,
            },
        ),
    ]
