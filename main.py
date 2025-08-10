
import YouTube_API
import database
from rich.pretty import pprint


def main():
    videoId = 'HMka55_hPqw'
    empty_token = ""
# initialize database with two tables: Comments and Replies
    s = set()
    c, conn = database.init()
    comments_list_response = []

    # make call to YouTube Data API
    comment_threads_list = YouTube_API.make_threads_request(
        videoId=videoId, pageToken=empty_token)

    # check what the data looks like
    print("calling insert_comment_threads")
    database.insert_comments(c, comment_threads_list)
    conn.commit()
    # Get parentIds
    p_ids_list = YouTube_API.get_pids(comment_threads_list)

    # make a separate call for each parentId in order to get comments results in a list
    print("going through parentIds")

    for pid in p_ids_list:
        s.add(pid)
    for pid in s:
        comments_list_response.append(
            YouTube_API.make_comment_request(pid, pageToken=empty_token))
    print("calling insert_replies")

    # add all found replies to database
    database.insert_replies(
        c, comments_list_response=comments_list_response)
    conn.commit()


if __name__ == "__main__":
    main()
