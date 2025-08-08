
import config
import googleapiclient.discovery
import draft
from rich.console import Console
from rich.pretty import pprint


def make_threads_request(videoId, pageToken: str):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = config.api_key

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=videoId,
        pageToken=pageToken,
        maxResults=100
    )
    comment_threads_list = []

    while request:
        response = request.execute()
        comment_threads_list.append(response)
        # continue paging until this returns None
        request = youtube.commentThreads().list_next(request, response)

    return comment_threads_list

# Can use parentId or Id as filter parameter
# The id parameter specifies a comma-separated list of comment IDs for the
# resources that are being retrieved. In a comment resource, the id property
# specifies the comment's ID.


def make_comment_request(id):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = config.api_key
    comments_list = []
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.comments().list(
        part="snippet",
        id=id,
    )
    comments_list.append(request.execute())


def read_replies(replies_list):
    # make replies table
    # the index witll be their id
    # and we will include metadata we want from replies

    # parse through comments list
    for comment in replies_list["snippet"]:
        print(comment)


def read_thread(thread_list):
    # response keys: 'kind', 'etag', 'nextPageToken', 'pageInfo', 'items'
    # total Results: total number of results in results set
    # resultsPerPage: number of results included in API response

    num_comments = 0
    totalResults = 0
    resultsPerPage = 0

    parentId_list = []

    # make table to print out comments
    table = draft.make_table()
    for thread in thread_list:

        totalResults = thread['pageInfo']['totalResults']
        resultsPerPage = thread['pageInfo']['resultsPerPage']

        for item in thread['items']:

            snippet_dict = item['snippet']
            # check if the comment has replies and if so print them out
            if 'replies' in item:
                # dictionary with the only key is comments
                replies = item['replies']
                for c in replies['comments']:
                    parentId_list.append(c['snippet']['parentId'])

                    #        topLevelComment_dict = snippet_dict['topLevelComment']
                    #        snippet_top_level_comment = topLevelComment_dict["snippet"]
                    #        id = topLevelComment_dict['id']
                    #        textOriginal = snippet_top_level_comment['textOriginal']
                    #        textDisplay = snippet_top_level_comment['textDisplay']
                    #        authorDisplayName = snippet_top_level_comment['authorDisplayName']
                    #        viewerRating = snippet_top_level_comment['viewerRating']
                    #        likeCount = snippet_top_level_comment['likeCount']
                    #        publishedAt = snippet_top_level_comment['publishedAt']
                    #        table.add_row(id, textOriginal, textDisplay, authorDisplayName, str(
                    #            viewerRating), str(likeCount), str(publishedAt))
                    #    num_comments += len(thread['items'])

                    # return the finished table
                    # console = Console()
                    # console.print(table)
                    # print("number of comments:", num_comments)
                    # print("total results:", totalResults)
                    # print("resultsPerPage:", resultsPerPage)

    return parentId_list
    # find snippet's keys: 'channelId', 'videoId','topLevelComment', 'canReply', 'totalReplyCount', 'isPublic']
    # snippet_dict = comment_thread['snippet']

    # topLevelComment keys: 'kind', 'etag', 'id', 'snippet'
    # topLevel_dict = snippet_dict["topLevelComment"]
    # snip_top_level = topLevel_dict["snippet"]

    # Snippet of topLevelComment keys: channelId', 'videoId', 'textDisplay', 'textOriginal',
    # 'authorDisplayName', 'authorProfileImageUrl', 'authorChannelUrl', 'authorChannelId',
    # 'canRate', 'viewerRating', 'likeCount', 'publishedAt', 'updatedAt'

    # comment Id
   # id = topLevel_dict['id']
   # # text
   # textOriginal = snip_top_level['textOriginal']
   # textDisplay = snip_top_level['textDisplay']
   # # author name
   # authorDisplayName = snip_top_level['authorDisplayName']
   # # viewer Rating
   # viewerRating = snip_top_level['viewerRating']
   # # likeCount
   # likeCount = snip_top_level['likeCount']
   # # publishedAt
   # publishedAt = snip_top_level['publishedAt']
   # print("getting comments...")

    # create dictionary to pass into sql database
    # data = {'id': id, 'authorDisplayName': authorDisplayName, 'textOriginal': textOriginal, 'textDisplay': textDisplay,
    #        'viewerRating': viewerRating, 'likeCount': likeCount, 'publishedAt': publishedAt}
#
# print(f"""
#      \ncomment id: {id}
#      \ntextOriginal: {textOriginal}
#      \ntextDisplay: {textDisplay}
#      \nauthorDisplayName: {authorDisplayName}
#      \nviewerRating: {viewerRating}
#      \nlikeCount: {likeCount}
#      \npublishedAt: {publishedAt}""")
#
# return data
