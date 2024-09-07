# BlueSky.py

Este projeto permite a extração de dados de perfis e postagens do Bluesky via API, salvando os dados em arquivos CSV. Ele inclui autenticação, extração de dados com paginação e salvamento de dados em formato legível.

## Funcionalidades
- Autenticação na API do Bluesky.
- Extração de dados de perfil e postagens de qualquer usuário do Bluesky.
- Realização de buscas por termos no Bluesky.
- Conversão dos dados para arquivos CSV.
- Reutilização de token de autenticação com suporte a `.env`.
- Reautenticação automática caso o token expire.

## Pré-requisitos

Antes de começar, você precisará ter os seguintes componentes instalados:

- Python 3.9+
- `pip` para gerenciar pacotes Python

### Instalação de dependências

No diretório raiz do projeto, execute o seguinte comando para instalar as dependências necessárias:

```bash
pip install -r requirements.txt
```
### Como autenticar
Crie um arquivo .env no diretório raiz do projeto.
Complete o .env com seu nome de usuário do Bluesky e uma App Password criada no caminho Settings -> Advanced -> App Passwords.

Exemplo do conteúdo do arquivo .env:

```bash
BLUESKY_APP_USER=seu_usuario.bsky.social
BLUESKY_APP_PASS=sua_app_password
```

## Como usar
### Extrair dados de um perfil
Para extrair dados de um perfil no Bluesky (como postagens, informações do usuário, etc.), execute o seguinte comando:

```bash
python main.py profile NOME_DO_USUARIO.BSKY.SOCIAL
```

Exemplo:

```bash
python main.py profile exemplo.bsky.social
```

### Realizar uma busca por termos
Para buscar postagens contendo um termo específico no Bluesky, utilize o modo de busca. O resultado será salvo em um arquivo CSV, com base no termo de busca e na data da execução.

```bash
python main.py search TERMO_DE_BUSCA --sort latest --limit 25
````

- --sort: Define a ordenação dos resultados. Pode ser latest (padrão) ou top.
- --limit: Define o número de posts por página (padrão: 25).

Exemplo de uso:

```bash
python main.py search tecnocracia --sort latest --limit 50
```

### Modo Verboso
Para aumentar a verbosidade da saída e receber mais detalhes durante o processo, utilize a flag --verbose em qualquer um dos modos:

```bash
python main.py search tecnocracia --verbose
```

### Como os dados são salvos
Os dados extraídos serão salvos na pasta ./data no formato CSV, e o nome do arquivo incluirá o termo de busca ou o nome do perfil e a data da extração.