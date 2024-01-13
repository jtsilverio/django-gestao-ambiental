# Generated by Django 4.2 on 2024-01-11 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cidades", "0001_initial"),
        ("destinacao", "0001_initial"),
        ("fornecedor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fornecedor",
            name="estado",
            field=models.CharField(
                choices=[
                    ("AC", "Acre"),
                    ("AL", "Alagoas"),
                    ("AP", "Amapá"),
                    ("AM", "Amazonas"),
                    ("BA", "Bahia"),
                    ("CE", "Ceará"),
                    ("DF", "Distrito Federal"),
                    ("ES", "Espírito Santo"),
                    ("GO", "Goiás"),
                    ("MA", "Maranhão"),
                    ("MT", "Mato Grosso"),
                    ("MS", "Mato Grosso do Sul"),
                    ("MG", "Minas Gerais"),
                    ("PA", "Pará"),
                    ("PB", "Paraíba"),
                    ("PR", "Paraná"),
                    ("PE", "Pernambuco"),
                    ("PI", "Piauí"),
                    ("RJ", "Rio de Janeiro"),
                    ("RN", "Rio Grande do Norte"),
                    ("RS", "Rio Grande do Sul"),
                    ("RO", "Rondônia"),
                    ("RR", "Roraima"),
                    ("SC", "Santa Catarina"),
                    ("SP", "São Paulo"),
                    ("SE", "Sergipe"),
                    ("TO", "Tocantins"),
                ],
                max_length=2,
                verbose_name="Estado",
            ),
        ),
        migrations.AlterField(
            model_name="fornecedor",
            name="id_cidade",
            field=models.ForeignKey(
                db_column="id_cidade",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="fornecedor",
                to="cidades.cidades",
                verbose_name="Cidade",
            ),
        ),
        migrations.AlterField(
            model_name="fornecedor",
            name="id_destinacao",
            field=models.ManyToManyField(
                blank=True,
                db_table="fornecedor_destinacao",
                related_name="fornecedor",
                to="destinacao.destinacao",
                verbose_name="Destinação",
            ),
        ),
        migrations.AlterField(
            model_name="fornecedor",
            name="id_tp_fornecedor",
            field=models.ManyToManyField(
                db_column="id_tp_fornecedor",
                db_table="fornecedor_tp_fornecedor",
                related_name="fornecedor",
                to="fornecedor.tipofornecedor",
                verbose_name="Tipo de Fornecedor",
            ),
        ),
        migrations.AlterField(
            model_name="fornecedor",
            name="nome",
            field=models.CharField(max_length=50, verbose_name="Nome"),
        ),
    ]
