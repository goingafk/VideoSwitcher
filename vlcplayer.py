import vlc
import keyboard
import time
import sys

instance = vlc.Instance()

player = instance.media_player_new()

default_path = 'default.mp4'
video1_path = 'video1.mp4'
video2_path = 'video2.mp4'

def play_video(video_path):
    media = instance.media_new(video_path)
    player.set_media(media)
    player.toggle_fullscreen()
    player.play()

def handle_keypress():
    while True:
        if keyboard.is_pressed('1'):
            play_video(default_path)
        
        elif keyboard.is_pressed('2'):
            play_video(video1_path)
        
        elif keyboard.is_pressed('3'):
            play_video(video2_path)
        
        elif keyboard.is_pressed('esc'):
            player.stop()
            sys.exit(0)
        
        time.sleep(0.1)


play_video(video1_path)
handle_keypress()