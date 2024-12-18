import sqlite3
import json

def update_sqlite(all_data):
    conn = sqlite3.connect('data/project.db')
    cursor = conn.cursor()
    
    for table, records in all_data.items():
        # Créer la table si elle n'existe pas
        if records:
            columns = list(records[0]['fields'].keys())
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table} ({', '.join([f'{col} TEXT' for col in columns])})"
            cursor.execute(create_table_query)
        
        # Insérer ou mettre à jour les données
        for record in records:
            fields = record['fields']
            placeholders = ', '.join(['?' for _ in fields])
            columns = ', '.join(fields.keys())
            values = tuple(json.dumps(v) if isinstance(v, (dict, list)) else v for v in fields.values())
            
            insert_query = f"INSERT OR REPLACE INTO {table} ({columns}) VALUES ({placeholders})"
            cursor.execute(insert_query, values)
    
    conn.commit()
    conn.close()
    print("SQLite database updated successfully")

if __name__ == "__main__":
    # Ce bloc ne sera exécuté que si le script est exécuté directement
    # et non pas importé comme un module
    pass
