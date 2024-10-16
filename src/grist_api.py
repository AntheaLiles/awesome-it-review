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
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data['records'])

# Fonction pour mettre à jour le fichier sur GitHub
def update_github_file(file_name, content):
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    
    file_path = f"data/{file_name}"  # Ajout du préfixe 'data/'
    
    try:
        # Essayez de récupérer le fichier existant
        file = repo.get_contents(file_path)
        repo.update_file(file_path, f"Update {file_name}", content, file.sha)
        print(f"File {file_path} updated successfully")
    except Exception as e:
        if "404" in str(e):
            # Si le fichier n'existe pas, créez-le
            repo.create_file(file_path, f"Create {file_name}", content)
            print(f"File {file_path} created successfully")
        else:
            # Si une autre erreur se produit, levez-la
            raise

# Liste des tables à mettre à jour
tables = ['Benchmark_Languages', 'Benchmark_Logiciels', 'Benchmark_Browsers', 'Benchmark_CLI', 'Benchmark_DBMS', 'Benchmark_FileFormats', 'Benchmark_FileSystem', 'Benchmark_Licences', 'Benchmark_OS', 'Benchmark_Ontologies', 'Benchmark_VisualParadigms', 'Benchmark_WidgetToolkit', 'Benchmark_WindowsManager', 'Benchmark_WorkingEnvironment']

# Mise à jour des données pour chaque table
for table in tables:
    try:
        df = get_grist_data(table)
        csv_content = df.to_csv(index=False)
        update_github_file(f"{table}.csv", csv_content)
    except Exception as e:
        print(f"Error processing table {table}: {str(e)}")

print("All tables processed")