from grist_api import get_all_grist_data
from update_sqlite import update_sqlite

def main():
    all_data = get_all_grist_data()
    update_sqlite(all_data)

if __name__ == "__main__":
    main()
