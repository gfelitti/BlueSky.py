import os
import pandas as pd
from datetime import datetime

def save_data_to_csv(profile_df, posts_df, username, full):
    simple_username = username.split(".")[0] if not full else username
    current_date = datetime.now().strftime("%Y_%m_%d")
    
    # Certificar-se de que o diretório 'data' existe
    os.makedirs("./data", exist_ok=True)
    
    profile_file = f"./data/{simple_username}_profile_{current_date}.csv"
    posts_file = f"./data/{simple_username}_posts_{current_date}.csv"
    
    profile_df.to_csv(profile_file, index=False)
    posts_df.to_csv(posts_file, index=False)
    
    print(f"Perfil salvo em {profile_file}")
    print(f"Postagens salvas em {posts_file}")
