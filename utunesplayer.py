import vlc

def play_rtmp(url):
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(url)
    player.set_media(media)
    player.play()
    
    while True:
        continue

url = "rtmp://home.paroxity.org:6969/live/music"
play_rtmp(url)
