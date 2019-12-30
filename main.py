import json
import readline
import urllib.request
from urllib.parse import quote

# auto complete source, the auto complete service should abstract to a dedicate server if it's huge and dynamic
source = [
    "about",
    "above",
    "across",
    "app",
    "apple",
    "appreciate",
    "bad",
    "ball",
    "balloon",
    "bell",
    "cat",
]


def completer(text, state):
    # iterate source to compare, it's better to use prefix tree
    options = [i for i in source if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None


readline.parse_and_bind("tab: complete")
readline.set_completer(completer)

while True:
    q = input("please input what gif you want\n\r")
    # url-encode input
    q = quote(q, 'utf-8')
    # search service can abstract to a dedicate server
    url = "http://api.giphy.com/v1/gifs/search?q=" + q + "&api_key=DLCVuTK6KZExOS7JoMq82bi5MaI6EbWO&limit=1"
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    data = response.read()
    values = json.loads(data)
    if values['data']:
        # regarding how to display gif on terminal
        # https://medium.com/youstart-labs/how-to-play-gif-in-your-terminal-d7657578e717
        print(values['data'][0]['images']['downsized_large']['url'])
    else:
        print("no result, pls try another")
