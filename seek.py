import vlc
import time
import keyboard
import sys

# Initialize VLC instance
instance = vlc.Instance()

# Create VLC media player
player = instance.media_player_new()

# Define the video path and time range (in milliseconds)
videoPath = 'video2_720p.mp4' #Consider renaming

video1StartTime = 1000
video1EndTime = 3000

video2StartTime = 5000
video2EndTime = 7000


video3StartTime = 0
video3EndTime = 0

video4StartTime = 0
video4EndTime = 0

instance = vlc.Instance('--verbose=2')  # Increase verbosity level
instance = vlc.Instance('--vout=opengl')


# Function to loop a video segment between startTime and endTime
def LoopVideoSegment(video_path):

    global video1StartTime, video1EndTime, video2StartTime, video2EndTime, video3StartTime, video3EndTime, video4StartTime, video4EndTime

    startTime = video1StartTime
    endTime = video1EndTime

    media = instance.media_new(video_path)
    player.set_media(media)
    player.set_fullscreen(True)

    # Start playing the video
    player.play()

    # Allow some time for the video to start
    time.sleep(0.1)

    # Loop the segment indefinitely
    while True:
        
        # Set the player to the start time (in milliseconds)
        player.set_time(startTime)

        # Continuously check the current playback time
        while player.get_time() < endTime:
            time.sleep(0.05)  # Small delay to prevent excessive CPU usage

            if (keyboard.is_pressed('esc')):
                player.stop()
                sys.exit(0)

            elif (keyboard.is_pressed('1')):
                startTime = video1StartTime
                endTime = video1EndTime
                player.set_time(startTime)

            elif (keyboard.is_pressed('2')):
                startTime = video2StartTime
                endTime = video2EndTime
                player.set_time(startTime)
            
            elif (keyboard.is_pressed('3')):
                pass # Add logic for key-press

            elif (keyboard.is_pressed('4')):
                pass # Add logic for key-press

        # Once the endTime is reached, the loop resets the video to the startTime
        player.set_time(startTime)

# Loop the video segment from 1 to 3 seconds
LoopVideoSegment(videoPath)
