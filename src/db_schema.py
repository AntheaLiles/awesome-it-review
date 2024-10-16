from sqlalchemy import create_engine, MetaData
import pydot

def generate_db_schema(database):
    # Créer une connexion à la base de données
    engine = create_engine(f'sqlite:///{database}')
    metadata = MetaData()
    metadata.reflect(bind=engine)
    
    # Créer un graphe
    graph = pydot.Dot(graph_type='digraph')
    
    # Ajouter les tables comme nœuds
    for table in metadata.tables.values():
        node = pydot.Node(table.name, shape="record", label=f"{table.name}|{' | '.join(column.name for column in table.columns)}")
        graph.add_node(node)
    
    # Ajouter les relations comme arêtes
    for table in metadata.tables.values():
        for fk in table.foreign_keys:
            edge = pydot.Edge(table.name, fk.column.table.name)
            graph.add_edge(edge)
    
    # Sauvegarder le schéma en SVG
    graph.write_svg('data/db_schema.svg')
    print("Schéma de la base de données généré avec succès.")

# Fonction utilitaire pour créer une connexion (peut être utile pour d'autres opérations)
def create_connection(database):
    try:
        engine = create_engine(f'sqlite:///{database}')
        return engine
    except Exception as e:
        print(f"Erreur lors de la connexion à la base de données: {e}")
        return None
