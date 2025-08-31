import re


def find_ids(link):
    match = re.search(r'[?&]v=([^&#]+)', link)
    if match:
        return match.group(1)
