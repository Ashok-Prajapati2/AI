from youtubesearchpython import *
import vlc
from pytube import YouTube
        

def Play(play):
       
        # customSearch = CustomSearch('movie', VideoSortOrder.uploadDate, limit = 1)
        # customSearch = CustomSearch('', VideoSortOrder.viewCount, limit=1)
        # query = "Mahabali Maharudra"
        query = play
        textSearch = query.replace(" ", "")

        customSearch = Hashtag(textSearch, limit = 1)

        results = customSearch.result()

        if results['result']:
        
        
            url = results['result'][0]['link']

            youtube = YouTube(f"{url}")
            video_stream = youtube.streams.get_highest_resolution()
            media = vlc.MediaPlayer(video_stream.url)
            media.play()

            while True:
                 pass
             
             
        else:
            print('No results found.')





