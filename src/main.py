from grist_api import get_all_grist_data
from update_sqlite import update_sqlite

def main():
    # Récupérer toutes les données de Grist
    all_data = get_all_grist_data()
    
    # Mettre à jour la base de données SQLite avec les données
    update_sqlite(all_data)

if __name__ == "__main__":
    main()
