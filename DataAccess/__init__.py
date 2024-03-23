from contextlib import contextmanager
import pymssql
import traceback

MSSQL_SERVER = "localhost"
MSSQL_DATABASE = "trac_nghiem"
MSSQL_PORT = "1433"


@contextmanager
def get_database(as_dict=True):
    mssql_connection = pymssql.connect(server=MSSQL_SERVER, database=MSSQL_DATABASE, port=MSSQL_PORT, as_dict=as_dict)
    cursor = mssql_connection.cursor()

    try:
        yield cursor
        mssql_connection.commit()
    except pymssql.Error:
        traceback.print_exc()
        mssql_connection.rollback()
        raise
    finally:
        mssql_connection.close()
