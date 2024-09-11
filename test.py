import vlc
import time
import keyboard
import sys

# Initialize VLC instance
instance = vlc.Instance()

# Create VLC media player
player = instance.media_player_new()

# Define the video path and time range (in milliseconds)
video_path = 'video.mp4'
v1_start = 1000
v1_end = 3000

v2_start = 5000
v2_end = 7000


# Function to loop a video segment between start_time and end_time
def loop_video_segment(video_path, start_time, end_time):

    global v1_start, v2_start, v1_end, v2_end

    start_time = v1_start
    end_time = v1_end

    media = instance.media_new(video_path)
    player.set_media(media)
    player.toggle_fullscreen()

    # Start playing the video
    player.play()

    # Allow some time for the video to start
    time.sleep(0.1)

    # Loop the segment indefinitely
    while True:
        
        # Set the player to the start time (in milliseconds)
        player.set_time(start_time)

        # Continuously check the current playback time
        while player.get_time() < end_time:
            current_time = player.get_time()
            #print(f"Current time: {current_time / 1000} seconds")  # Show time in seconds
            time.sleep(0.05)  # Small delay to prevent excessive CPU usage

            if(keyboard.is_pressed('esc')):
                player.stop()
                sys.exit(0)
            elif(keyboard.is_pressed('1')):
                start_time = v1_start
                end_time = v1_end
                player.set_time(start_time)
            elif(keyboard.is_pressed('2')):
                start_time = v2_start
                end_time = v2_end
                player.set_time(start_time)

        # Once the end_time is reached, the loop resets the video to the start_time
        #print(f"Looping back to {start_time / 1000} seconds")
        player.set_time(start_time)


start_time = 1000  # 1 second in milliseconds
end_time = 5000    # 3 seconds in milliseconds

# Loop the video segment from 1 to 3 seconds
loop_video_segment(video_path, v1_start, v1_end)
