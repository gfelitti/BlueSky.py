import os
import pandas as pd
from datetime import datetime

def save_data_to_csv(profile_df, posts_df, username, full):
    simple_username = username if full else username.split(".")[0]
    current_date = datetime.now().strftime("%Y_%m_%d")
    
    # Certificar-se de que o diretório 'data' existe
    os.makedirs("./data", exist_ok=True)
    
    profile_file = f"./data/{simple_username}_profile_{current_date}.csv"
    posts_file = f"./data/{simple_username}_posts_{current_date}.csv"
    
    profile_df.to_csv(profile_file, index=False)
    posts_df.to_csv(posts_file, index=False)
    
    num_rows = len(posts_df)
    print(f"Perfil salvo em {profile_file}")
    print(f"{num_rows} postagens salvas em {posts_file}")

def save_search_data_to_csv(posts_df, query):
    """
    Função para salvar os dados de posts de busca em um arquivo CSV.

    Args:
    - posts_df: DataFrame contendo os posts retornados pela API de busca.
    - query: Termo de busca utilizado para identificar o arquivo.

    Salva:
    - Um arquivo CSV contendo os dados dos posts retornados pela API de busca.
    """
    
    # Obter a data atual no formato AAAA_MM_DD
    current_date = datetime.now().strftime("%Y_%m_%d")
    
    # Definir o nome do arquivo com base no termo de busca e data
    search_file = f"./data/search_results_{query}_{current_date}.csv"
    
    # Garantir que o diretório 'data' existe
    os.makedirs("./data", exist_ok=True)
    num_rows = len(posts_df)
    # Salvar os posts no arquivo CSV
    posts_df.to_csv(search_file, index=False, encoding='utf-8')
    
    print(f"{num_rows} resultados da busca salvos em {search_file}")