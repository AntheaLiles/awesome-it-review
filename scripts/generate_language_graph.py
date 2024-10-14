import pandas as pd
import ast
import json
import os

def generate_language_data():
    # Lire le CSV
    df = pd.read_csv('data/Benchmark_Languages.csv')
    df['fields'] = df['fields'].apply(ast.literal_eval)
    df['Naissance'] = df['fields'].apply(lambda x: x.get('Naissance'))
    
    # Filtrer les entrées sans année de naissance
    df = df[df['Naissance'].notna()]
    
    # Convertir en entier et grouper par décennie
    df['Décennie'] = (df['Naissance'].astype(int) // 10) * 10
    language_counts = df['Décennie'].value_counts().sort_index()
    
    # Créer le dossier 'data' s'il n'existe pas
    os.makedirs('data', exist_ok=True)
    
    # Sauvegarder les données du graphique en JSON
    with open('data/languages_per_decade_data.json', 'w') as f:
        json.dump({'x': language_counts.index.tolist(), 'y': language_counts.values.tolist()}, f)

if __name__ == "__main__":
    generate_language_data()