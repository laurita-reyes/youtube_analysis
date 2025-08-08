
import YouTube_API
from rich.pretty import pprint


def main():
    videoId = 'HMka55_hPqw'
    empty_token = ""
    reply_count = 0
    # make call to YouTube Data API
    comment_threads_list = YouTube_API.make_threads_request(
        videoId=videoId, pageToken=empty_token)

    p_ids_list = YouTube_API.read_thread(comment_threads_list)
    for id in p_ids_list:
        pprint(id)

        # YouTube_API.read_replies(comments_list)
        # make request to fetch comments list
        # YouTube_API.make_comment_request()
        # reply_count += len(comments_list)

        # for each reply ID make a request to the API for the comment data
     #   for id in reply_ids:
     #       reply_comment_response = YouTube_API.make_comment_request(id)
     #       print(reply_comment_response)
     #   print("reply counts:", reply_count)
        #


if __name__ == "__main__":
    main()
