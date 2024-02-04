# importing time and vlc
import time
import vlc
from youtubesearchpython import Hashtag
from pytube import YouTube

# method to play video
def play_video(source):
    # creating a vlc instance
    vlc_instance = vlc.Instance()

    # creating a media player
    player = vlc_instance.media_player_new()

    # creating a media
    media = vlc_instance.media_new(source)

    # setting media to the player
    player.set_media(media)

    # play the video
    player.play()

    # wait time
    time.sleep(0.5)

    # getting the duration of the video
    duration = player.get_length()

    # printing the duration of the video
    print("Duration : " + str(duration))

    while True:
        pass

# method to get video URL
def get_video_url():
    custom_search = Hashtag('song', limit=1)
    results = custom_search.result()

    if results['result']:
        url = results['result'][0]['link']
        return url
    else:
        return None

# get video URL
video_url = get_video_url()

if video_url:
    # call the video method
    play_video(video_url)
else:
    print('No results found.')
