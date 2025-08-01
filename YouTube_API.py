import config
from rich import print
import googleapiclient.discovery


def make_request(videoId, pageToken):
    api_service_name = "youtube"
    api_version = "v3"

    DEVELOPER_KEY = config.api_key

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=videoId,
        pageToken=pageToken,
        maxResults=50
    )
    response = request.execute()
    print(f"response: {response}")
    return response


def get_comments(request):

    response_dicts = request

    # response keys: 'kind', 'etag', 'nextPageToken', 'pageInfo', 'items'
    # total Results: total number of results in results set
    # resultsPerPage: number of results included in API response

    # pageInfo = response_dicts['pageInfo']
    nextPageToken = response_dicts['nextPageToken']
    # if there is a nextPageToken

    # print(f"{pageInfo['totalResults']}")
    # print(f"{pageInfo['resultsPerPage']}")

    # comment_thread_dicts = response_dicts['items']
    comment_thread = response_dicts['items'][0]

    # find snippet's keys: 'channelId', 'videoId','topLevelComment', 'canReply', 'totalReplyCount', 'isPublic']
    snippet_dict = comment_thread['snippet']

    # topLevelComment keys: 'kind', 'etag', 'id', 'snippet'
    topLevel_dict = snippet_dict["topLevelComment"]
    snip_top_level = topLevel_dict["snippet"]

    # Snippet of topLevelComment keys: channelId', 'videoId', 'textDisplay', 'textOriginal',
    # 'authorDisplayName', 'authorProfileImageUrl', 'authorChannelUrl', 'authorChannelId',
    # 'canRate', 'viewerRating', 'likeCount', 'publishedAt', 'updatedAt'

    # comment Id
    id = topLevel_dict['id']
    # text
    textOriginal = snip_top_level['textOriginal']
    textDisplay = snip_top_level['textDisplay']
    # author name
    authorDisplayName = snip_top_level['authorDisplayName']
    # viewer Rating
    viewerRating = snip_top_level['viewerRating']
    # likeCount
    likeCount = snip_top_level['likeCount']
    # publishedAt
    publishedAt = snip_top_level['publishedAt']
    print("getting comments...")
    # create dictionary to pass into sql database
    data = {'id': id, 'authorDisplayName': authorDisplayName, 'textOriginal': textOriginal, 'textDisplay': textDisplay,
            'viewerRating': viewerRating, 'likeCount': likeCount, 'publishedAt': publishedAt}

    print(f"""
          \ncomment id: {id}
          \ntextOriginal: {textOriginal}
          \ntextDisplay: {textDisplay}
          \nauthorDisplayName: {authorDisplayName}
          \nviewerRating: {viewerRating} 
          \nlikeCount: {likeCount}
          \npublishedAt: {publishedAt}""")

    return data
