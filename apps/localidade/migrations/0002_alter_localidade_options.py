# Generated by Django 4.2 on 2023-05-22 16:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("localidade", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="localidade",
            options={
                "ordering": ["-id_localidade"],
                "verbose_name": "Localidade",
                "verbose_name_plural": "Localidades",
            },
        ),
    ]
