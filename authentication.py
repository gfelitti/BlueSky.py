import os
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def get_token():
    token = os.getenv("BLUESKY_APP_TOKEN")

    # Se o token não estiver definido, tenta autenticar usando o username e password
    if not token:
        token = authenticate_bluesky()
        # Você pode optar por armazenar o token no .env ou em outro lugar após a primeira autenticação
        print("Token gerado, por favor, adicione o seguinte ao seu arquivo .env:")
        print(f"BLUESKY_APP_TOKEN={token}")
    return token

def authenticate_bluesky():
    username = os.getenv("BLUESKY_APP_USER")
    password = os.getenv("BLUESKY_APP_PASS")

    if not username or not password:
        raise ValueError("Variáveis de ambiente BLUESKY_APP_USER e BLUESKY_APP_PASS devem ser definidas.")

    url = "https://bsky.social/xrpc/com.atproto.server.createSession"
    response = requests.post(
        url,
        json={"identifier": username, "password": password}
    )
    
    if response.status_code != 200:
        raise ValueError("Erro ao tentar fazer login no Bluesky. Verifique suas credenciais.")
    
    return response.json()['accessJwt']  # Retorna o token de autenticação
