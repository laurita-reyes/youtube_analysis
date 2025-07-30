import sqlite3
import pandas as pd


def init_database():
    conn = sqlite3.connect("comments_db.sqlite")
    c = conn.cursor()
    # create table in db
    query = """CREATE TABLE Comments(id, username, text_original,text_display, viewer_rating, like_count, published_at)"""
    c.execute(query)


def insert(data, con):
    stmt = "INSERT INTO YouTube_Comments VALUES(?,?,?,?,?,?,?)"
    con.execute()
