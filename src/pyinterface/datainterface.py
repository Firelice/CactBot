import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """

    conn = sqlite3.connect(db_file)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """

    c = conn.cursor()
    c.execute(create_table_sql)


conn = create_connection("discord.db")
c = conn.cursor()


def create():
    """
    creates tables
    :return:
    """
    create_table(conn, """CREATE TABLE IF NOT EXISTS ffid (
                                            id INTEGER PRIMARY KEY,
                                            ffname text NOT NULL,
                                            discordID integer
                                                            );""")
    create_table(conn, """CREATE TABLE IF NOT EXISTS ffid (
                                            id integer PRIMARY KEY,
                                            discordID integer,
                                            drops text,
                                            typedrop text,
                                            job text
                                                            );""")


def insert_chara(name, ID):
    create()
    with conn:
        c.execute("INSERT INTO ffid(ffname, discordID) VALUES (:ffname, :discordID)", {'ffname': name, 'discordID': ID})




