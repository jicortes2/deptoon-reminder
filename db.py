from psycopg2 import connect, IntegrityError
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
import urllib.parse as urlparse

"""
CREATE TABLE reminders (chat_id VARCHAR(50) NOT NULL, reminder TEXT NOT NULL,
                date DATE NOT NULL, type INT NOT NULL, finished BOOLEAN DEFAULT FALSE);
CREATE INDEX chats_index ON reminders (chat_id);
"""

def _access(option=True):
    """ Returns connection to splitbot database  """
    return connect(
                    dbname=os.environ["DB_NAME"],
                    user=os.environ["DB_USER"],
                    password=os.environ["DB_PASS"],
                    host=os.environ["DB_HOST"],
                    port=os.environ["DB_PORT"]
                )


def add_element(table, thing, sender_id):
    """ Returns true if the thing is added to the table """
    try:
        conn = _access()
        cur = conn.cursor()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur.execute("INSERT INTO {} (idea, date, owner) VALUES ('{}', NULL, {})".format(table, thing, sender_id))
        conn.close()
        return True
    except IntegrityError:
        return False
