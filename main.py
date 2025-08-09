
import YouTube_API
from rich.pretty import pprint


def main():
    videoId = 'HMka55_hPqw'
    empty_token = ""
    reply_count = 0
    comments_list_response = []
    # make call to YouTube Data API
    comment_threads_list = YouTube_API.make_threads_request(
        videoId=videoId, pageToken=empty_token)
    
    p_ids_list = YouTube_API.read_thread(comment_threads_list)
    # parent IDs for comments
  
    # make a separate call for each parentId and save results in a list
    for pid in p_ids_list:
        comments_list_response.append(YouTube_API.make_comment_request(pid, pageToken=empty_token))
        
    # list of comments list responses
    YouTube_API.read_replies(comments_list_response)
        
    
   
        

    
if __name__ == "__main__":
    main()
