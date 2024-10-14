import pandas as pd
import plotly.graph_objects as go
import ast
import os
import json

def generate_language_graph():
    # Lire le CSV
    df = pd.read_csv('data/Benchmark_Languages.csv')
    df['fields'] = df['fields'].apply(ast.literal_eval)
    df['Naissance'] = df['fields'].apply(lambda x: x.get('Naissance'))
    
    # Grouper par décennie
    df['Décennie'] = (df['Naissance'] // 10) * 10
    language_counts = df['Décennie'].value_counts().sort_index()
    
    # Créer le graphique avec Plotly
    fig = go.Figure(data=[go.Bar(x=language_counts.index, y=language_counts.values)])
    
    fig.update_layout(
        title='Nombre de langages créés par décennie',
        xaxis_title='Décennie de création',
        yaxis_title='Nombre de langages',
        xaxis=dict(tickmode='array', tickvals=language_counts.index, ticktext=[f"{year}s" for year in language_counts.index])
    )
    
    # Créer le dossier 'images' s'il n'existe pas
    os.makedirs('images', exist_ok=True)
    
    # Sauvegarder le graphique en format HTML
    fig.write_html('images/languages_per_decade.html', full_html=False, include_plotlyjs='cdn')
    
    # Sauvegarder les données du graphique en JSON pour une utilisation ultérieure si nécessaire
    with open('images/languages_per_decade_data.json', 'w') as f:
        json.dump({'x': language_counts.index.tolist(), 'y': language_counts.values.tolist()}, f)

if __name__ == "__main__":
    generate_language_graph()
