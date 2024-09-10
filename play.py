import vlc
import time

videoPath = "video2.mp4"

instance = vlc.Instance()

player = instance.media_player_new()

def play_video():
    media = instance.media_new(videoPath)
    player.set_media(media)
    player.set_fullscreen(True)
    player.play()

play_video()

while True:
    command = input().lower()

    if(command=='p'):
        player.pause()
    elif(command=='r'):
        player.play()
    elif(command=='s'):
        player.stop()
        break
    time.sleep(1)