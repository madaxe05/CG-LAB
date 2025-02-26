import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bresenham's Line Drawing Algorithm")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def bresenham_line(x0, y0, x1, y1):
    # Determine the differences
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    # Determine the direction of the step
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    
    # Initialize the error term
    err = dx - dy
    
    while True:
        # Draw the current pixel
        pygame.draw.circle(window, WHITE, (x0, y0), 1)
        
        # Check if we have reached the end point
        if x0 == x1 and y0 == y1:
            break
        
        # Calculate the error terms
        e2 = 2 * err
        
        # Adjust the error term and coordinates
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def main():
    # Set up initial and end points
    x0, y0 = 100, 100
    x1, y1 = 700, 500
    
    # Fill the background
    window.fill(BLACK)
    
    # Draw the line using Bresenham's algorithm
    bresenham_line(x0, y0, x1, y1)
    
    # Update the display
    pygame.display.update()
    
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
