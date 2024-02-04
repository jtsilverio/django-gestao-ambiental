# Created manually on 2023-10-22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("entrada", "0001_initial"),
        ("saida", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE VIEW resumo_mensal_residuos AS
            SELECT ROW_NUMBER() OVER () AS id, *
            FROM (
                SELECT
                    'entrada' AS tipo,
                    EXTRACT(YEAR FROM data) AS ano,
                    EXTRACT(MONTH FROM data) AS mes,
                    l.nome  AS cluster,
                    tp.nome  AS tp_residuos,
                    SUM(quantidade) AS quantidade,
                    0 AS receita,
                    0 AS custo
                FROM entrada e
                JOIN cluster l
                    ON e.id_cluster = l.id
                JOIN tipo_residuos tp
                    ON e.id_tp_residuos  = tp.id
                GROUP BY ano, mes, cluster, tp_residuos

                UNION ALL

                SELECT
                    'saida' AS tipo,
                    EXTRACT(YEAR FROM data) AS ano,
                    EXTRACT(MONTH FROM data) AS mes,
                    l.nome  AS cluster,
                    tp.nome  AS tp_residuos,
                    SUM(quantidade) AS quantidade,
                    SUM(receita) AS receita,
                    SUM(custo) AS custo
                FROM saida s
                JOIN cluster l
                    ON s.id_cluster = l.id
                JOIN tipo_residuos tp
                    ON s.id_tp_residuos  = tp.id
                GROUP BY ano, mes, cluster, tp_residuos
            ) AS resumo_mensal_residuos;
            """,
            reverse_sql="DROP VIEW resumo_mensal_residuos;",
        )
    ]
