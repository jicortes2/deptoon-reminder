from psycopg2 import connect, IntegrityError
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
import urllib.parse as urlparse

"""
CREATE TABLE reminders (chat_id BIGINT NOT NULL, reminder TEXT NOT NULL,
                date DATE NOT NULL, type INT NOT NULL, finished BOOLEAN DEFAULT FALSE);
CREATE INDEX chats_index ON reminders (chat_id);
"""

def _access(option=True):
    """ Returns connection to deptoon reminder database  """
    return connect(
                    dbname=os.environ["DB_NAME"],
                    user=os.environ["DB_USER"],
                    password=os.environ["DB_PASS"],
                    host=os.environ["DB_HOST"],
                    port=os.environ["DB_PORT"]
                )


def add_reminder(chat_id, periodicity, date, msg):
    """ Returns true if the thing is added to the table """
    try:
        conn = _access()
        cur = conn.cursor()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        query = "INSERT INTO reminders (chat_id, reminder, date, type) VALUES \
                ({}, '{}', '{}', {})".format(chat_id, msg, date, periodicity)
        print(query)
        cur.execute(query)
        conn.close()
        return True
    except IntegrityError:
        return False

def find_reminders():
    """ Returns reminders from today """
    conn = _access()
    cur = conn.cursor()
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    query = 'SELECT * FROM reminders \
             WHERE EXTRACT(month FROM "date") = EXTRACT(month FROM now()) AND\
             EXTRACT(day FROM "date") = EXTRACT(day FROM now()) AND \
             finished = FALSE'
    cur.execute(query)
    tuples = cur.fetchAll()
    conn.close()
    return tuples
