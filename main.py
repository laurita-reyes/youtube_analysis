
import YouTube_API

def main():
    videoId = 'HMka55_hPqw'
    empty_token = ""
    # make call to YouTube Data API
    comment_threads_list = YouTube_API.make_request(
        videoId=videoId,pageToken=empty_token)
    YouTube_API.read_thread(comment_threads_list)

if __name__ == "__main__":
    main()
