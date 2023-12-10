# Gestão Ambiental
A enviromental management CRUD made in Django.

# Set up para desenvolvimento:
## Váriaveis de ambiente
```
make django-env-vars
```

Nesse projeto é usado o pacote `environ` para administrar as variáveis de ambiente   dentro do arquivo `.env`. As variáveis de ambiente requeridas são:
  - `SECRET_KEY`: Uma chave secreta gerada pelo Django para proteção de formuários e cookies
    - A chave secreta pode ser gerada e setada dentro do `.env` automaticamente usando o comando `make django-secret-key`.
  - `DEBUG`: Uma flag booleana que indica se estamos em um ambiente de produção ou de desenvolvimento. Se estivermos em um ambiente de desenvolvimento, o valor dessa flag deve ser atribuido manualmente como `True`.

## Gestão de dependências
```
make install_requirements
```

As dependências do projeto são listadas dentro do `pyproject.toml` e compiladas para o `requirements.txt` usando o comando `make requirements`. Esse comando usa o `pip-tools` para compilar todas dependências e gerar um hash para cada uma delas. 

Com o `requirements.txt` gerado, pode-se instalar as dependências usando apenas o `pip install -r requirements.txt`. Para facilitar o processo de instalação, o comando `make install_requirements` pode ser usado para realizar todo processo de instalar o pip-tools, compilar os requirements e instalar as dependências dentro do ambiente python.


# Frontend Theme:
- https://demo.themesberg.com/volt/pages/dashboard/dashboard.html
- https://themesberg.com/docs/volt-bootstrap-5-dashboard/components/widgets/
