
import YouTube_API
import database
from rich.pretty import pprint
import link_extractor


def main():

    print("enter youtube url:")
    url = input()
    # youtube video ID
    video_id = link_extractor.find_ids(url)

    print(video_id)
    s = set()
    c, conn = database.init()
    comments_list_response = []

    empty_token = ""
    # initialize database with two tables: Comments and Replies
    # make call to YouTube Data API
    comment_threads_list = YouTube_API.make_threads_request(
        videoId=video_id, pageToken=empty_token)

    print("calling insert_comment_threads")
    database.insert_comments(c, comment_threads_list)
    conn.commit()

    # Get parentIds
    p_ids_list = YouTube_API.get_pids(comment_threads_list)
    # make a separate call for each parentId in order to get comments results in a list
    print("going through parentIds")
    for pid in p_ids_list:
        print(f"pid:{pid}")
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
