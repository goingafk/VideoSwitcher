import vlc
import time

videoPath = "video2.mp4"

instance = vlc.Instance()

player = instance.media_player_new()

def play_video():
    media = instance.media_new(videoPath)
    player.set_media(media)
    player.play()

play_video()

while True:
    state = player.get_state()
    if state == vlc.State.Ended:
        play_video()
    time.sleep(1)