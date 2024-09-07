import requests

def get_profile_data(username, token):
    """
    Função para obter os dados de perfil de um usuário do Bluesky.
    
    Args:
    - username: Nome de usuário do Bluesky.
    - token: Token de autenticação.
    
    Retorna:
    - Dados do perfil em formato JSON, ou None se houver erro.
    """
    url = f"https://bsky.social/xrpc/app.bsky.actor.getProfile?actor={username}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code < 200 or response.status_code >= 300:
        print(f"Erro ao obter perfil: {response.status_code}")
        return None
    
    return response.json()

def get_all_posts(username, token):
    """
    Função para obter todas as postagens de um perfil no Bluesky.
    
    Args:
    - username: Nome de usuário do Bluesky.
    - token: Token de autenticação.
    
    Retorna:
    - Lista de postagens do usuário.
    """
    posts = []
    cursor = None
    
    url = "https://bsky.social/xrpc/app.bsky.feed.getAuthorFeed"
    
    while True:
        params = {
            "actor": username,
            "limit": 100
        }
        
        if cursor:
            params["cursor"] = cursor
        
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code < 200 or response.status_code >= 300:
            print(f"Aviso: Código de status inesperado ao obter posts: {response.status_code}")
            break
        
        data = response.json()
        
        if 'feed' not in data or not data['feed']:
            break
        
        posts.extend(data['feed'])
        cursor = data.get('cursor')
        
        if not cursor:
            break
    
    return posts


def search_posts(query, token, sort="latest", limit=25):
    posts = []
    
    url = "https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts"
    
    # Definir apenas os parâmetros essenciais
    params = {
        "q": query,
        "sort": sort,
        "limit": limit
    }
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers, params=params)

    #print(f"Status Code: {response.status_code}")
    #print(f"Resposta da API: {response.text}")
    
    if response.status_code != 200:
        print(f"Aviso: Código de status inesperado ao buscar posts: {response.status_code}")
        return []

    try:
        data = response.json()
    except ValueError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return []
    
    #print(f"Dados retornados pela API: {data}")
    
    # Verifique se a chave 'posts' está presente
    if 'posts' not in data or not data['posts']:
        print(f"Sem dados na chave 'posts'. Dados retornados: {data}")
        return []
    
    # Adicionar os posts à lista
    posts.extend(data['posts'])
    
    return posts
