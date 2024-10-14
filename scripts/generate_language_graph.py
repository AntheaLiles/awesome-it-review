import pandas as pd
import matplotlib.pyplot as plt
import ast

def generate_language_graph():
    # Lire le CSV
    df = pd.read_csv('data/Benchmark_Languages.csv')
    df['fields'] = df['fields'].apply(ast.literal_eval)
    df['Naissance'] = df['fields'].apply(lambda x: x.get('Naissance'))
    language_counts = df['Naissance'].value_counts().sort_index()
    
    # Créer le graphique
    plt.figure(figsize=(12, 6))
    language_counts.plot(kind='bar')
    plt.title('Nombre de langages créés par année')
    plt.xlabel('Année de création')
    plt.ylabel('Nombre de langages')
    plt.tight_layout()
    
    # Sauvegarder le graphique
    plt.savefig('images/languages_per_year.svg', format='svg')
    plt.close()

if __name__ == "__main__":
    generate_language_graph()
