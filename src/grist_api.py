import os
import requests
import json
from github import Github

# Configuration
GRIST_API_KEY = os.environ['GRIST_API_KEY']
GRIST_DOC_ID = os.environ['GRIST_DOC_ID']
GITHUB_TOKEN = os.environ['ACTIONS_TOKEN']
REPO_NAME = 'AntheaLiles/awesome-it-review'

def get_grist_data(table_name):
    url = f"https://docs.getgrist.com/api/docs/{GRIST_DOC_ID}/tables/{table_name}/records"
    headers = {"Authorization": f"Bearer {GRIST_API_KEY}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['records']

def get_all_grist_data():
    tables = ['Benchmark_Languages', 'Benchmark_Logiciels', 'Benchmark_Browsers', 'Benchmark_CLI', 'Benchmark_DBMS', 'Benchmark_FileFormats', 'Benchmark_FileSystem', 'Benchmark_Licences', 'Benchmark_OS', 'Benchmark_Ontologies', 'Benchmark_VisualParadigms', 'Benchmark_WidgetToolkit', 'Benchmark_WindowsManager', 'Benchmark_WorkingEnvironment']

    all_data = {}
    for table in tables:
        try:
            all_data[table] = get_grist_data(table)
            print(f"Data for {table} fetched successfully")
        except Exception as e:
            print(f"Error processing table {table}: {str(e)}")

    print("All tables processed")
    return all_data

# Si vous voulez exécuter le script directement
if __name__ == "__main__":
    data = get_all_grist_data()
    # Vous pouvez faire quelque chose avec 'data' ici si nécessaire
