import pandas as pd
import json
import ast
import os

def generate_language_data():
    df = pd.read_csv('data/Benchmark_Languages.csv')
    df['fields'] = df['fields'].apply(ast.literal_eval)
    df['Naissance'] = df['fields'].apply(lambda x: x.get('Naissance'))
    df = df[df['Naissance'].notna()]
    df['Décennie'] = (df['Naissance'].astype(int) // 10) * 10
    language_counts = df['Décennie'].value_counts().sort_index()
    
    data = {
        'x': language_counts.index.tolist(),
        'y': language_counts.values.tolist(),
        'type': 'bar'
    }
    
    os.makedirs('data', exist_ok=True)
    with open('data/languages_per_decade_data.json', 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    generate_language_data()
