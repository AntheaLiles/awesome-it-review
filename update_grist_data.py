import os
import requests
import pandas as pd
from github import Github

# Configuration
GRIST_API_KEY = os.environ['GRIST_API_KEY']
GRIST_DOC_ID = os.environ['GRIST_DOC_ID']
GITHUB_TOKEN = os.environ['ACTIONS_TOKEN']
REPO_NAME = 'AntheaLiles/it-review'

# Fonction pour récupérer les données de Grist
def get_grist_data(table_name):
    url = f"https://docs.getgrist.com/api/docs/{GRIST_DOC_ID}/tables/{table_name}/records"
    headers = {"Authorization": f"Bearer {GRIST_API_KEY}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return pd.DataFrame(data['records'])

# Fonction pour mettre à jour le fichier sur GitHub
def update_github_file(file_name, content):
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    
    try:
        # Essayez de récupérer le fichier existant
        file = repo.get_contents(file_name)
        repo.update_file(file_name, f"Update {file_name}", content, file.sha)
        print(f"File {file_name} updated successfully")
    except:
        # Si le fichier n'existe pas, créez-le
        repo.create_file(file_name, f"Create {file_name}", content)
        print(f"File {file_name} created successfully")

# Liste des tables à mettre à jour
tables = ['Benchmark_Languages', 'Benchmark_Logiciels', 'Benchmark_Browsers']  # Remplacez par les noms de vos tables Grist

# Mise à jour des données pour chaque table
for table in tables:
    df = get_grist_data(table)
    csv_content = df.to_csv(index=False)
    update_github_file(f"{table}.csv", csv_content)

print("All tables updated successfully")
