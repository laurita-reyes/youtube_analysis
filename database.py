import sqlite3
import YouTube_API
from rich import print

# initialize database and create datatable.


def init_database():
    conn = sqlite3.connect("comments_db.sqlite")
    c = conn.cursor()

    # create table in db
    query = """CREATE TABLE IF NOT EXISTS Comments(id, username, text_original, text_display, viewer_rating, like_count, published_at)"""
    c.execute(query)


def add_comments(data, con):
    stmt = "INSERT INTO YouTube_Comments VALUES(?,?,?,?,?,?,?)"
    con.execute()
