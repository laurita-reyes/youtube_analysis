import requests
# make API call and store the response

url = f"""https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.commentThreads.list?part=snippet%2Creplies&
videoId=YiGfOEj9K0U"""
r = requests.get(url)

# Check Status code
status_code = r.status_code
print(f'Status Code: {status_code}')

# store API response
