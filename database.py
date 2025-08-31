import sqlite3
from rich.pretty import pprint


# initialize database and create datatable.
def init():
    conn = sqlite3.connect("youtube_data_db.sqlite")
    c = conn.cursor()

    # create table in db
    query = """CREATE TABLE IF NOT EXISTS Comments( id PRIMARY KEY , username, text_original, text_display, viewer_rating, like_count, published_at)"""
    query2 = """CREATE TABLE IF NOT EXISTS Replies ( id  PRIMARY KEY, username, text_original, text_display, viewer_rating, like_count, published_at)"""
    c.execute(query)
    c.execute(query2)
    return c, conn


def insert_comments(cur, threads_list):
    num_comments = 0
    print("indexing dictionary...")
    for thread in threads_list:

        for item in thread['items']:

            snippet_dict = item['snippet']
            # check if the comment has replies and if so print them out
            topLevelComment_dict = snippet_dict['topLevelComment']
            snippet_top_level_comment = topLevelComment_dict["snippet"]

            id = topLevelComment_dict['id']
            textOriginal = snippet_top_level_comment['textOriginal']
            textDisplay = snippet_top_level_comment['textDisplay']
            authorDisplayName = snippet_top_level_comment['authorDisplayName']
            viewerRating = snippet_top_level_comment['viewerRating']
            likeCount = snippet_top_level_comment['likeCount']
            publishedAt = snippet_top_level_comment['publishedAt']
            cur.execute(
                '''INSERT INTO Comments VALUES (?, ?, ?, ?, ?, ?, ?)''',
                (id, authorDisplayName, textOriginal, textDisplay, viewerRating, likeCount, publishedAt))
            pprint(f"""id: {id}, textOriginal:{textOriginal}, textDisplay: {textDisplay}, authorDisplayName: {authorDisplayName},
                  viewerRating: {viewerRating}, likeCount: {likeCount}, publishedAt: {publishedAt}""")

            num_comments += len(thread['items'])


def insert_replies(cur, comments_list_response):

    print("indexing dictionary...")
    for list in comments_list_response:

        for response in list:
            pprint(response['pageInfo'])
            if 'totalResults' in response['pageInfo']:
                totalResults = response['pageInfo']['totalResults']
                print(totalResults)
            for item in response['items']:
                # pprint(item)
                id = item['id']
                snippet_dict = item['snippet']
                authorDisplayName = snippet_dict['authorDisplayName']
                textDisplay = snippet_dict['textDisplay']
                textOriginal = snippet_dict['textOriginal']
                viewerRating = snippet_dict['viewerRating']
                likeCount = snippet_dict['likeCount']
                publishedAt = snippet_dict['publishedAt']

                cur.execute(
                    '''INSERT INTO Replies VALUES (?, ?, ?, ?, ?, ?, ?)''',
                    (id, authorDisplayName, textOriginal, textDisplay, viewerRating, likeCount, publishedAt))
                pprint(f"""id: {id}, authorDisplayName:{authorDisplayName}, textOriginal: {textOriginal} ,textDisplay:{textDisplay}, viewerRating:{viewerRating}, likeCount: {likeCount},
                              publishedAt:{publishedAt}""")
