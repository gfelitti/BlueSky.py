import argparse
from authentication import get_token
from data_extraction import get_profile_data, get_all_posts, search_posts
from data_conversion import convert_profile_to_df, convert_posts_to_df, convert_search_to_df
from data_saving import save_data_to_csv, save_search_data_to_csv

def extract_profile_data(username, token, full):
    """
    Função para extrair dados de um perfil e suas postagens.
    
    Args:
    - username: Nome de usuário no Bluesky.
    - token: Token de autenticação.
    """
    # Obtenção dos dados do perfil e posts
    profile_data = get_profile_data(username, token)
    posts_data = get_all_posts(username, token)

    if profile_data and posts_data:
        print(f"Dados obtidos com sucesso para: {username}")
        
        # Converter os dados para DataFrames
        profile_df = convert_profile_to_df(profile_data)
        posts_df = convert_posts_to_df(posts_data)
        
        # Salvar os dados em CSV
        save_data_to_csv(profile_df, posts_df, username, full)
    else:
        print(f"Erro ao obter perfil ou posts para o perfil: {username}")

def extract_search_data(query, token, sort, limit):
    """
    Função para extrair dados de busca com base nos parâmetros fornecidos.
    
    Args:
    - query: Termo de busca.
    - token: Token de autenticação.
    - Outros parâmetros opcionais de filtro e ordenação.
    """
    # Obtenção dos dados da busca
    posts_data = search_posts(query, token, sort, limit)

    if posts_data:
        print(f"Dados de busca obtidos com sucesso para o termo: {query}")
        
        # Converter os dados para DataFrame
        posts_df = convert_search_to_df(posts_data)
        
        # Salvar os dados em CSV
        save_search_data_to_csv(posts_df, query)
    else:
        print(f"Nenhum dado encontrado para o termo de busca: {query}")

if __name__ == "__main__":
    # Configuração do parser de argumentos
    parser = argparse.ArgumentParser(description="Extrair dados de perfis ou buscar posts no Bluesky e salvar em CSV.")
    
    # Argumento para modo de operação (profile ou search)
    parser.add_argument(
        "mode",
        type=str,
        choices=["profile", "search"],
        help="Escolha o modo de extração: 'profile' para extrair dados de perfil ou 'search' para buscar posts."
    )
    
    # Identificador para o modo (username ou termo de busca)
    parser.add_argument(
        "identifier",
        type=str,
        help="Nome de usuário (no modo 'profile') ou termo de busca (no modo 'search')."
    )
    
    # Parâmetros opcionais para o modo 'search'
    parser.add_argument("--sort", type=str, choices=["top", "latest"], default="latest", help="Ordenação dos resultados da busca (top ou latest).")
    parser.add_argument("--limit", type=int, default=25, help="Limite de resultados por página (padrão: 25).")

    
    # Argumento opcional para modo verboso
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Aumentar a verbosidade da saída."
    )

    # Argumento opcional para salvar o nome de usuário completo
    parser.add_argument(
        "-f", "--full",
        action="store_true",
        help="Salva o nome completo do usuário."
    )

    # Parseia os argumentos passados na linha de comando
    args = parser.parse_args()

    # Obtenção do token de autenticação
    token = get_token()

    if args.verbose:
        print(f"Iniciando a coleta de dados no modo: {args.mode} para o identificador: {args.identifier}")
    
    # Escolher o modo de operação: perfil ou busca
    if args.mode == "profile":
        print(args.identifier)
        extract_profile_data(args.identifier, token, args.full)
    elif args.mode == "search":
        extract_search_data(
            args.identifier, token, args.sort, args.limit)
    if args.verbose:
        print(f"Finalizado o processo para o usuário: {args.identifier}")
