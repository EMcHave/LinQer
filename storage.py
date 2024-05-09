import sqlite3
from const import table_name, db_name


def create_table():
    with sqlite3.connect(db_name) as db:
        db.execute(
            f"""CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY,
                    link_url TEXT NOT NULL,
                    user_id INTEGER NOT NULL
                    )"""
        )
        db.commit()


def get_link(id_chat):
    with sqlite3.connect(db_name) as db:
        cursor = db.execute(
            f"SELECT * FROM {table_name} WHERE user_id='{id_chat}' ORDER BY RANDOM() LIMIT 1"
        )
        link = cursor.fetchone()
        if link:
            db.execute(
                f"DELETE FROM {table_name} WHERE id='{link[0]}' AND link_url='{link[1]}'"
            )
            db.commit()
            return link[1]
        else:
            return None


def insert_link(article, user_id):
    with sqlite3.connect(db_name) as db:
        db.execute(
            f"INSERT INTO {table_name} (link_url, user_id) VALUES ('{article}', '{user_id}')"
        )
        db.commit()


def check_link_existence(text, user_id):
    with sqlite3.connect(db_name) as db:
        cursor = db.execute(
            f"SELECT * FROM {table_name} WHERE user_id='{user_id}' AND link_url='{text}'"
        )
        article = cursor.fetchone()
        return bool(article)
