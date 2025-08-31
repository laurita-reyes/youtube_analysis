import requests
import config
import html
topic = "hasan"
url = f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q={topic}&key={config.api_key}"
r = requests.get(url)

response = r.json()
for video in response['items']:
    title = html.unescape(video['snippet']['title'])
    print(f"Video Title: {title}")
