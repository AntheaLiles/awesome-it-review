from grist_api import get_all_grist_data
from update_sqlite import update_sqlite
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
from sqlalchemy_schemadisplay import create_schema_graph

def generate_db_schema():
    engine = create_engine('sqlite:///data/project.db')
    metadata = MetaData()
    metadata.reflect(bind=engine)
    graph = create_schema_graph(metadata=metadata)
    graph.write_svg('data/db_schema.svg')

def main():
    all_data = get_all_grist_data()
    update_sqlite(all_data)
    generate_db_schema()

if __name__ == "__main__":
    main()
