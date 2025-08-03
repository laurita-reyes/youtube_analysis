from dataclasses import dataclass
from typing import Dict,List,Literal,Optional


@dataclass
class ApiParameters:
    part:Literal["id", "snippet", "replies"]
    filters:Literal["allThreadsRelatedToChannelId", "id","videoId","maxResults"]
    maxResults:Optional[int]
    pageToken:Optional[str]

@dataclass Snippet
@dataclass
class CommentThread:
    kind:str
    etag:str
    id:
@dataclass
class CommentThreadInfo:
    totalResults:int
    resultsPerPage:int
@dataclass
class CommentThreadResponse:
    kind: str
    etag: str
    nextPageToken:Optional[str]
    pageInfo: CommentThreadInfo
    items:List[Dict]
