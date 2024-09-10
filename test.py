import pygame
import av
import numpy as np
 
# Initialize Pygame
pygame.init()
 
# Open the video file with pyav
video_file = 'video2.mp4'
container = av.open(video_file)
stream = container.streams.video[0]
 
# Get video dimensions
width = stream.width
height = stream.height
 
# Set up Pygame display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PyAV Video Player')
 
# Clock to control frame rate
clock = pygame.time.Clock()
 
# Function to convert av frame to a pygame surface
def av_frame_to_surface(frame):
    # Convert the frame to a numpy array
    img = frame.to_ndarray(format='rgb24')
    # Convert numpy array to pygame surface
    return pygame.surfarray.make_surface(np.transpose(img, (1, 0, 2)))
 
# Main loop
running = True
for packet in container.demux(stream):
    for frame in packet.decode():
        # Convert AV frame to Pygame surface
        surface = av_frame_to_surface(frame)
 
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
 
        # Display the frame
        screen.blit(surface, (0, 0))
        pygame.display.flip()
 
        # Control frame rate
        #clock.tick(stream.rate / stream.time_base)
 
# Clean up
pygame.quit()