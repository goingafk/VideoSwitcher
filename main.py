import moviepy.editor as mp
import pygame
import sys

# Initialize Pygame
pygame.init()

# Load two videos
default = mp.VideoFileClip("default.mp4")
video1 = mp.VideoFileClip("video1.mp4")
video2 = mp.VideoFileClip("video3.mp4")

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Set up Pygame display with the size of the first video
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Clock to control frame rate
clock = pygame.time.Clock()

def preload_frames(video):
    frames = []
    for frame in video.iter_frames(fps = video.fps, dtype = "uint8"):
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        frames.append(frame_surface)
    return frames

default_frames = preload_frames(default)
video1_frames = preload_frames(video1)
video2_frames = preload_frames(video2)

# Function to play the video in a loop and handle video switching
def play_video(video_frames, fps):
    for frame_surface in video_frames:
        screen.blit(frame_surface, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 1
                elif event.key == pygame.K_2:
                    return 2
                elif event.key == pygame.K_3:
                    return 3

        # Control frame rate
        clock.tick(fps)

# Main loop
current_video = 1  # Start with the first video
try:
    while True:
        if current_video == 1:
            next_video = play_video(default_frames, default.fps)
        elif current_video == 2:
            next_video = play_video(video1_frames, video1.fps)
        elif current_video == 3:
            next_video = play_video(video2_frames, video2.fps)
        
        # Update current video based on user input
        if next_video:
            current_video = next_video
except KeyboardInterrupt:
    pygame.quit()
    sys.exit()
