import requests

def get_profile_data(username, token):
    url = f"https://bsky.social/xrpc/app.bsky.actor.getProfile?actor={username}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code < 200 or response.status_code >= 300:
        print(f"Erro ao obter perfil: {response.status_code}")
        return None
    
    return response.json()

def get_all_posts(username, token):
    posts = []
    cursor = None
    while True:
        url = "https://bsky.social/xrpc/app.bsky.feed.getAuthorFeed"
        params = {"actor": username, "limit": 100}
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
