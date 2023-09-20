from datetime import datetime, timedelta

#from django.db.models import Sum
#from django.http import HttpResponse
from django.shortcuts import render

from apps.home.models import EntradaMensal, SaidaMensal
import plotly.express as px
#import pandas as pd


def get_mothly_dataframe(year: int):
    monthly_dic = {}
    cont = 0  # contador para índice
    for data in list(EntradaMensal.objects.filter(ano=year).all().values()):
        del data['id']
        data['peso'] = float(data['peso'])
        data['tipo'] = 'entrada'
        monthly_dic[cont] = data
        cont += 1
    
    for data in list(SaidaMensal.objects.filter(ano=year).all().values()):
        del data['id']
        data['peso'] = float(data['peso'])
        data['receita'] = float(data['receita'])
        data['custo'] = float(data["custo"])
        data['tipo'] = 'saida'
        monthly_dic[cont] = data
        cont += 1
    
    return monthly_dic


def get_dashboard_stats(monthly_dic):
    current_month = datetime.now().month-1
    dashboard_stats = {}
    for tipo_dado in ["entrada", "saida"]:
        print('\n')
        current_month_peso = sum(v['peso'] for v in monthly_dic.values() if v['mes'] == current_month and v['tipo'] == tipo_dado)  # monthly_dataframe.loc[(monthly_dataframe["mes"] == current_month) & (monthly_dataframe["tipo"] == tipo_dado), "peso",].sum()

        last_month_peso = sum(v['peso'] for v in monthly_dic.values() if v['mes'] == current_month - 1 and v['tipo'] == tipo_dado)  # last_month_peso = monthly_dataframe.loc[(monthly_dataframe["mes"] == current_date.month - 1) & (monthly_dataframe["tipo"] == tipo_dado), "peso",].sum()
        
        diff = current_month_peso - last_month_peso
        diff_perc = 100 * (diff / last_month_peso) if last_month_peso else (9999 if current_month_peso else 0)
        # convert to int
        diff_perc = int(diff_perc)
        trend = "up" if last_month_peso <= current_month_peso  else "down"

        dashboard_stats[tipo_dado] = {
            "current_month_peso": current_month_peso,
            "diff": diff,
            "diff_perc": diff_perc,
            "trend": trend,
        }
        print(tipo_dado)
        print('peso_atual', current_month_peso)
        print('peso_anterior', last_month_peso)
        print('diff', diff)
        print('diff_perc', diff_perc)
        print('trend', trend)

    dashboard_stats["saldo"] = {
        "current_month_peso": dashboard_stats["entrada"]["current_month_peso"] - dashboard_stats["saida"]["current_month_peso"],
        "diff": dashboard_stats["entrada"]["diff"] - dashboard_stats["saida"]["diff"],
        "diff_perc": dashboard_stats["entrada"]["diff_perc"] - dashboard_stats["saida"]["diff_perc"],
        "trend": 'up' if dashboard_stats["entrada"]["current_month_peso"] >= dashboard_stats["saida"]["current_month_peso"] else 'down',
    }

    return dashboard_stats


def monthly_lineplot(monthly_dic):
    dic = {}
    # Encontre o ano e mês mínimo e máximo na tabela original
    ano_minimo = min(values['ano'] for values in monthly_dic.values())
    ano_maximo = max(values['ano'] for values in monthly_dic.values())
    mes_minimo = min(values['mes'] for values in monthly_dic.values())
    mes_maximo = max(values['mes'] for values in monthly_dic.values())
    
    for ano in range(ano_minimo, ano_maximo + 1):
        for mes in range(mes_minimo, mes_maximo + 1):
            for tipo in list(set(values['tipo'] for values in monthly_dic.values())):
                chave = (ano, mes, tipo)
                if chave not in dic:
                    dic[chave] = {'mes': mes, 'tipo': tipo, 'peso': 0, 'ano': ano}
                    
    for values in monthly_dic.values():
        mes = values['mes']
        tipo = values['tipo']
        peso = values['peso']
        ano = values['ano']
        
        chave = (ano, mes, tipo)  # Usar uma tupla como chave para evitar duplicatas
        dic[chave]['peso'] += peso
    
    # criar uma lista de dicionários a partir do dicionário
    lista_de_dicionarios = sorted(list(dic.values()), key=lambda x: (x['ano'], x['mes'], x['tipo']))

    for dicionario in lista_de_dicionarios:
        print(dicionario)
    print(len(lista_de_dicionarios))

    plot = px.line(
        lista_de_dicionarios,
        x='mes',
        y='peso',
        color='tipo',
        labels={'peso': "Peso (kg)", 'mes': "Mês", "ano": "Ano"},
        markers=True,
        template="plotly_white",
        line_shape="spline",
        color_discrete_map={
            "entrada": "#31316A",
            "saida": "#F3C78D",
        },
    )
    plot.update_xaxes(type="category")
    plot.update_traces(
        line=dict(width=5),
        marker=dict(size=9),
        hovertemplate=None)
    plot.update_layout(
        margin=dict(l=5, r=5, t=5, b=5),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            title=None,
        ),
        plot_bgcolor= "rgba(0, 0, 0, 0)",
        paper_bgcolor= "rgba(0, 0, 0, 0)",
        hovermode="x unified",
    )
    config = {"displayModeBar": False}

    return plot.to_html(
        full_html=False,
        default_height=350,
        div_id="line-plot",
        config=config,
    )


def home(request):
    current_date = datetime.now()
    monthly_dic = get_mothly_dataframe(current_date.year)

    dashboard_stats = get_dashboard_stats(monthly_dic)
    plot = monthly_lineplot(monthly_dic)

    context = {
        "stats_dict": dashboard_stats,
        "plot": plot,
    }

    return render(request, "home/home.html", context)
