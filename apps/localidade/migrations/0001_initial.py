# Generated by Django 4.2.6 on 2023-10-29 15:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Localidade",
            fields=[
                ("id_localidade", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Localidade",
                "verbose_name_plural": "Localidades",
                "db_table": "localidade",
                "ordering": ["nome"],
            },
        ),
    ]
