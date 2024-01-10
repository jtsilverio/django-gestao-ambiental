# Generated by Django 4.2 on 2024-01-04 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cidades", "0001_initial"),
        ("destinacao", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TipoFornecedor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "nome",
                    models.CharField(
                        choices=[
                            ("Transporte", "Transporte de Resíduos"),
                            ("Destinação Final", "Destinação Final de Resíduos"),
                            ("Serviço de Terceiros", "Serviço de Terceiros"),
                        ],
                        max_length=25,
                    ),
                ),
            ],
            options={
                "verbose_name": "Tipo de Fornecedor",
                "verbose_name_plural": "Tipos de Fornecedores",
                "db_table": "tipo_fornecedor",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Fornecedor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=50)),
                (
                    "estado",
                    models.CharField(
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
                    ),
                ),
                (
                    "id_cidade",
                    models.ForeignKey(
                        db_column="id_cidade",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="fornecedor",
                        to="cidades.cidades",
                    ),
                ),
                (
                    "id_destinacao",
                    models.ManyToManyField(
                        blank=True,
                        db_table="fornecedor_destinacao",
                        related_name="fornecedor",
                        to="destinacao.destinacao",
                    ),
                ),
                (
                    "id_tp_fornecedor",
                    models.ManyToManyField(
                        db_column="id_tp_fornecedor",
                        db_table="fornecedor_tp_fornecedor",
                        related_name="fornecedor",
                        to="fornecedor.tipofornecedor",
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
