# Generated by Django 4.2 on 2023-05-15 12:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("saida", "0002_rename_mtr_saida_n_evidencia"),
    ]

    operations = [
        migrations.AlterField(
            model_name="saida",
            name="cdf",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
