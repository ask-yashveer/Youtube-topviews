#--This program is taking Channel id for example- "UCWN3xxRkmTPmbKwht9FuE5A" and "UCxX9wt5FWQUAAz4UrysqK9A"--
#--and not for example "marquesbrownlee" as input. Silimar videos are displayed according to the video title--
#--so, there maybe a possiblity  repeation of urls in some the cases.--

import urllib.request
import json
import re
from urllib.parse import urljoin
import urllib.parse
#--Function to get Top 100 Videos of a channel using Channel ID--
def function(channel_id):
    c=0
    api_key = 'AIzaSyCG7HtEu9W5edkSL-juzie7sajNj-6FAMc'
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=viewcount&maxResults=25'.format(api_key, channel_id)
    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)
        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])
        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    print('Top 100 Videos')
    for x in range(len(video_links)):
        if c<100:
            print("Position: ",x+1)
            title=function2('https://www.youtube.com/oembed?format=json&url='+video_links[x],video_links[x])
            c=c+1
            function3(title)
        else:
            break

#--Function to get title, channel name in json format--

def function2(id,ur):
    url = 'https://www.youtube.com/oembed?format=json&url='
    json1 = json.load(urllib.request.urlopen(id))
    title = json1['title']
    author = json1['author_name']
    print("Title: %s\nChannel: %s\nURL: %s\n" % (title, author, ur))
    return title

#--Function to find similar videos according to the video title--

def function3(title):
    query_string = urllib.parse.urlencode({"search_query": title})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    print("Five Similar Videos")
    for x in range(2,11,2):
        print("http://www.youtube.com/watch?v=" + search_results[x])
    print("------------------------------------------------------------------------------------------------------------")

name = input("Enter Channel ID: ")
function(name)
