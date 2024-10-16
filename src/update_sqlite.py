import sqlite3
import pandas as pd
import os

def update_sqlite():
    conn = sqlite3.connect('data/project.db')
    
    tables = ['Benchmark_Languages', 'Benchmark_Logiciels', 'Benchmark_Browsers', 'Benchmark_CLI', 'Benchmark_DBMS', 'Benchmark_FileFormats', 'Benchmark_FileSystem', 'Benchmark_Licences', 'Benchmark_OS', 'Benchmark_Ontologies', 'Benchmark_VisualParadigms', 'Benchmark_WidgetToolkit', 'Benchmark_WindowsManager', 'Benchmark_WorkingEnvironment']
    
    for table in tables:
        csv_path = f'data/{table}.csv'
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            df.to_sql(table, conn, if_exists='replace', index=False)
        else:
            print(f"Warning: {csv_path} not found")
    
    conn.close()

if __name__ == "__main__":
    update_sqlite()
