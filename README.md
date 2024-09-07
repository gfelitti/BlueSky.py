# BlueSky.py

Este projeto permite a extração de dados de perfis e postagens do Bluesky via API, salvando os dados em arquivos CSV. Ele inclui autenticação, extração de dados com paginação e salvamento de dados em formato legível.

## Funcionalidades
- Autenticação na API do Bluesky.
- Extração de dados de perfil e postagens de qualquer usuário do Bluesky.
- Conversão dos dados para arquivos CSV.
- Reutilização de token de autenticação com suporte a `.env`.

## Pré-requisitos

Antes de começar, você precisará ter os seguintes componentes instalados:

- Python +3.9
- `pip` para gerenciar pacotes Python

### Instalação de dependências

No diretório raiz do projeto, execute o seguinte comando para instalar as dependências necessárias:

```bash
pip install -r requirements.txt
```

### Como autenticar

Complete o .env com seu nome de usuário e um App Password criado Settings -> Advanced -> App Passwords

## Como usar

No terminal, rode main.py com o nome do usuário cujos posts você quer extrair.

```bash
python main.py PERFIL-BLUESKY.BSKY.SOCIAL
```