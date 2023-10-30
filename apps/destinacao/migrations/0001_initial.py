# Generated by Django 4.2.6 on 2023-10-30 23:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Destinacao",
            fields=[
                ("id_destinacao", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Destinação",
                "verbose_name_plural": "Destinações",
                "db_table": "destinacao",
                "ordering": ["nome"],
            },
        ),
    ]
