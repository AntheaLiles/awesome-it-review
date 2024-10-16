from grist_api import get_all_grist_data
from update_sqlite import update_sqlite
from db_schema import generate_db_schema

def main():
    all_data = get_all_grist_data()
    update_sqlite(all_data)
    database = "data/project.db"
    generate_db_schema(database)

if __name__ == "__main__":
    main()
