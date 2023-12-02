MENU_SIDEBAR = [
    {
        "name": "Dashboard",
        "url": "home",
        "icon": "bi bi-bar-chart-line-fill ",
    },
    {
        "name": "Resíduos",
        "icon": "bi bi-trash3-fill",
        "submenu": [
            {
                "name": "Entrada",
                "url": "entrada",
            },
            {
                "name": "Saída",
                "url": "saida",
            },
        ],
    },
    {
        "name": "Fugitivas",
        "icon": "bi bi-fan",
        "submenu": [
            {
                "name": "AC e Extintores",
                "url": "ac_extintores:index",
            },
            {
                "name": "SF6 e NF3",
                "url": "ac_extintores:index",
            },
        ],
    },
    {
        "name": "Água",
        "url": "agua:index",
        "icon": "bi bi-droplet-fill",
    },
    {
        "name": "Eletricidade",
        "url": "eletricidade:index",
        "icon": "bi bi-lightning-charge-fill",
    },
    {
        "name": "Combustível",
        "url": "combustivel:index",
        "icon": "bi bi-fuel-pump-fill",
    },
    {"name": "div"},
    {
        "name": "Clusters",
        "url": "cluster:index",
        "icon": "bi bi-globe-americas",
    },
    {"name": "Tipo Resíduos", "url": "tipo_residuos:index", "icon": "bi bi-trash-fill"},
    {"name": "Destinação Resíduos", "url": "destinacao", "icon": "bi bi-recycle"},
    {
        "name": "Tipos Combustível",
        "url": "tipo_combustivel:index",
        "icon": "bi bi-fuel-pump-fill",
    },
    {
        "name": "Unidades Consumo",
        "url": "unidade_consumo:index",
        "icon": "bi bi-building-fill-gear",
    },
    {
        "name": "Fornecedores",
        "url": "fornecedor",
        "icon": "bi bi-shop",
    },
    {"name": "div"},
    {
        "name": "Admin",
        "url": "admin:index",
        "icon": "bi bi-gear-fill",
    },
]
