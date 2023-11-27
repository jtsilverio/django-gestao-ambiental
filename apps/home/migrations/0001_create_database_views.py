# Created manually on 2023-10-22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE VIEW resumo_mensal_residuos AS
            SELECT CAST(ROW_NUMBER() OVER () AS INTEGER) AS id, *
            FROM (
            SELECT
                'entrada' AS tipo,
                strftime('%Y', data) AS ano,
                strftime('%m', data) AS mes,
                l.nome  AS cluster,
                tp.nome  AS tp_residuos,
                peso AS peso,
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
                strftime('%Y', data) AS ano,
                strftime('%m', data) AS mes,
                l.nome  AS cluster,
                tp.nome  AS tp_residuos,
                peso AS peso,
                receita AS receita,
                custo AS custo
            FROM saida s
            JOIN cluster l
                ON s.id_cluster = l.id
            JOIN tipo_residuos tp
                ON s.id_tp_residuos  = tp.id
            GROUP BY ano, mes, cluster, tp_residuos
            )
            """,
            reverse_sql="DROP VIEW resumo_mensal_residuos;",
        )
    ]
