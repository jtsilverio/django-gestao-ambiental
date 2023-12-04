# Gestão Ambiental
A enviromental management CRUD made in Django.

# Set up para desenvolvimento:
## Criar arquivo `.env`
Nesse projeto estamos usando o pacote `environ` para administrar as variáveis de ambiente requeridas pelo projeto. Assim, na pasta raiz do projeto devemos criar um arquivo `.env` que contem as variáveis de ambiente usadas pelo sistema:
  - `SECRET_KEY`: Uma chave secreta gerada pelo Django para proteção de formuários e cookies
  - `DEBUG`: Uma flag booleana que indica se estamos em um ambiente de produção ou de desenvolvimento.

2. Para setarmos as variáveis no `.env`
  - Dentro da pasta raiz do projeto crie um arquivo chamado `.env`.
  - Se estiver em um ambiente UNIX rode `make django-secret-key`.
    - Esse comando gera uma nova chave secreta e cola ela dentro do `.env`.
  - Se estiver em um ambiente windows, devemos gerar e colar manualmente dentro do `.env`
    - Para isso dentro do interpretador python faça:
      ```
      from django.core.management.utils import get_random_secret_key
      print("SECRET_KEY=" + get_random_secret_key())
      ```
      - Cole o output desse comando no arquivo `.env`
  - Para setar o debug como True, caso em esteja em um ambiente de desenvolvimento, abra o `.env` adicione `DEBUG=True`.

# Frontend Theme:
- https://demo.themesberg.com/volt/pages/dashboard/dashboard.html
- https://themesberg.com/docs/volt-bootstrap-5-dashboard/components/widgets/

- 
