import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def get_table_names(conn):
    cur = conn.cursor()
    # cur.execute("SELECT color_id, khipu_id, cord_id, color_cd_1, color_cd_2, color_cd_3, color_cd_4, color_cd_5, ")
    cur.execute("SELECT KHIPU_ID, CORD_ID, CLUSTER_ID FROM cord_cluster")

    rows = cur.fetchall()

    for row in rows:
        print(row)


## tables:
## archive_dc              canuto_cluster          knot_cluster
## ascher_canutito_color   color_operator_dc       knot_type_dc
## ascher_canuto_color     cord                    pigmentation_dc
## ascher_color_dc         cord_classification_dc  primary_cord
## ascher_cord_color       cord_cluster            regions_dc
## attachment_dc           fiber_dc                structure_dc
## beginning_dc            grouping_class_dc       termination_dc
## canutito                khipu_main
## canuto                  knot

def main():
    database = r"C:\sqlite\db\khipu.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("Get table names:")
        get_table_names(conn)


if __name__ == '__main__':
    main()
