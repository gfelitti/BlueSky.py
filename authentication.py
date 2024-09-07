import os
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def authenticate_bluesky(username, password):
    """
    Função para autenticar-se no Bluesky e obter o token.
    
    Args:
    - username: Nome de usuário do Bluesky.
    - password: Senha do Bluesky.
    
    Retorna:
    - Token de autenticação.
    """
    url = "https://bsky.social/xrpc/com.atproto.server.createSession"
    response = requests.post(
        url,
        json={
            "identifier": username,
            "password": password
        }
    )
    
    if response.status_code != 200:
        raise Exception("Erro ao tentar fazer login no Bluesky. Verifique suas credenciais.")
    
    data = response.json()
    token = data.get('accessJwt')
    
    if not token:
        raise Exception("Falha ao obter o token de autenticação.")
    
    print("Autenticação realizada com sucesso.")
    
    # Opcional: Salvar o token no ambiente ou arquivo temporário
    os.environ["BLUESKY_ACCESS_TOKEN"] = token
    
    return token

def get_token():
    """
    Função para obter o token de autenticação do Bluesky.
    Se o token expirar, refaz a autenticação.
    
    Retorna:
    - Token de autenticação válido.
    """
    token = os.getenv("BLUESKY_ACCESS_TOKEN")
    if token:
        return token
    
    # Refaça a autenticação se o token não estiver disponível ou expirado
    username = os.getenv("BLUESKY_APP_USER")
    password = os.getenv("BLUESKY_APP_PASS")
    
    if not username or not password:
        raise Exception("As credenciais do Bluesky não estão configuradas.")
    
    return authenticate_bluesky(username, password)

def handle_token_expiration(response, username, password):
    """
    Verifica se a resposta da API indica token expirado e refaz a autenticação.
    
    Args:
    - response: Resposta da API.
    
    Retorna:
    - Token de autenticação renovado se o token estiver expirado.
    """
    if response.status_code == 401:  # Verifica se o token está expirado
        print("Token expirado. Reautenticando...")
        return authenticate_bluesky(username, password)
    return None
