
import config
import googleapiclient.discovery
import draft
from rich.console import Console
from rich.pretty import pprint
# response keys: 'kind', 'etag', 'nextPageToken', 'pageInfo', 'items'
# total Results: total number of results in results set
# resultsPerPage: number of results included in API response

# find snippet's keys: 'channelId', 'videoId','topLevelComment', 'canReply', 'totalReplyCount', 'isPublic']
# snippet_dict = comment_thread['snippet']

# topLevelComment keys: 'kind', 'etag', 'id', 'snippet'
# topLevel_dict = snippet_dict["topLevelComment"]
# snip_top_level = topLevel_dict["snippet"]

# Snippet of topLevelComment keys: channelId', 'videoId', 'textDisplay', 'textOriginal',
# 'authorDisplayName', 'authorProfileImageUrl', 'authorChannelUrl', 'authorChannelId',
# 'canRate', 'viewerRating', 'likeCount', 'publishedAt', 'updatedAt'


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


def make_comment_request(pid, pageToken: str):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = config.api_key

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.comments().list(
        part="snippet",
        parentId=pid,
        pageToken=pageToken,
        maxResults=20
    )
    comments_response_list = []
    while request:
        response = request.execute()
        comments_response_list.append(response)
        # continue paging until this returns None
        request = youtube.comments().list_next(request, response)

    # we want the list of it
    return comments_response_list


def read_replies(comments_list_response):

    num_replies = 0
    totalResults = 0
    resultsPerPage = 0

    table = draft.make_table()
    for list in comments_list_response:

        for response in list:
            pprint(response['pageInfo'])
            if 'totalResults' in response['pageInfo']:
                totalResults = response['pageInfo']['totalResults']
            pprint(len(response['items']))

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

                table.add_row(id, textOriginal, textDisplay, authorDisplayName, str(
                    viewerRating), str(likeCount), str(publishedAt))

    # return the finished table
    console = Console()
    console.print(table)

    print("number of replies:", num_replies)
    print("total results:", totalResults)
    print("resultsPerPage:", resultsPerPage)
    return


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

                topLevelComment_dict = snippet_dict['topLevelComment']
                snippet_top_level_comment = topLevelComment_dict["snippet"]
                id = topLevelComment_dict['id']
                textOriginal = snippet_top_level_comment['textOriginal']
                textDisplay = snippet_top_level_comment['textDisplay']
                authorDisplayName = snippet_top_level_comment['authorDisplayName']
                viewerRating = snippet_top_level_comment['viewerRating']
                likeCount = snippet_top_level_comment['likeCount']
                publishedAt = snippet_top_level_comment['publishedAt']
                table.add_row(id, textOriginal, textDisplay, authorDisplayName, str(
                    viewerRating), str(likeCount), str(publishedAt))

        num_comments += len(thread['items'])

    # return the finished table
    console = Console()
    console.print(table)
    print("number of comments:", num_comments)
    print("total results:", totalResults)
    print("resultsPerPage:", resultsPerPage)

    return parentId_list


# return data
