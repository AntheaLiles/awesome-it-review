import csv
import ast
import os

def csv_to_markdown(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Lire les en-têtes
        
        # Lire la première ligne de données pour obtenir les clés du dictionnaire
        first_row = next(reader)
        data_dict = ast.literal_eval(first_row[1])
        field_names = list(data_dict.keys())
        
        markdown = f"# {os.path.splitext(os.path.basename(csv_file))[0]}\n\n"
        markdown += "| id | " + " | ".join(field_names) + " |\n"
        markdown += "|---" + "|---" * len(field_names) + "|\n"
        
        # Remettre le curseur au début du fichier et sauter la ligne d'en-tête
        file.seek(0)
        next(reader)
        
        for row in reader:
            id_value = row[0]
            data_dict = ast.literal_eval(row[1])
            markdown += f"| {id_value} | " + " | ".join(str(data_dict.get(field, "")) for field in field_names) + " |\n"
    
    return markdown

def process_csv_files():
    data_dir = 'data'  # Dossier contenant les fichiers CSV
    for file in os.listdir(data_dir):
        if file.endswith('.csv'):
            csv_path = os.path.join(data_dir, file)
            markdown_content = csv_to_markdown(csv_path)
            md_file_path = f"{os.path.splitext(file)[0]}.md"
            with open(md_file_path, 'w', encoding='utf-8') as md_file:
                md_file.write(markdown_content)

if __name__ == "__main__":
    process_csv_files()
