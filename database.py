from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

connection_string = 'mysql://root@localhost/history_sqlalchemy'

engine = create_engine(connection_string, pool_pre_ping=True)
alembic_connection_string = connection_string

Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def map_keys_to_values(cols, values):
    def map_cols_to_values(col_values):
        return {col: val for (col, val) in zip(cols, col_values)}
    return list(map(map_cols_to_values, values))


def query_stpos_cache(query):
    with session_scope() as session:
        results = session.execute(text(query))
        #  return map_keys_to_values(results.keys(), results.fetchall())

