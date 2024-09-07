import argparse
from authentication import get_token
from data_extraction import get_profile_data, get_all_posts
from data_conversion import convert_profile_to_df, convert_posts_to_df
from data_saving import save_data_to_csv

def main(username, full):
    # Obtém o token da variável de ambiente ou autentica
    token = get_token()

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extrair dados de perfil e postagens de usuários do Bluesky e salvar em CSV.")
    
    # Argumento para nome de usuário
    parser.add_argument(
        "username",
        type=str,
        help="Nome de usuário no Bluesky (sem o @)."
    )
    
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
    
    if args.verbose:
        print(f"Iniciando a coleta de dados para o usuário: {args.username}")
    
    main(args.username, args.full)
    
    if args.verbose:
        print(f"Finalizado o processo para o usuário: {args.username}")
