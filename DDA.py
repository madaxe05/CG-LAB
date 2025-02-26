import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def dda_line(x0, y0, x1, y1):
    # Calculate dx and dy
    dx = x1 - x0
    dy = y1 - y0
    
    # Determine the number of steps needed
    steps = max(abs(dx), abs(dy))
    
    # Calculate the increment for each step
    x_increment = dx / steps
    y_increment = dy / steps
    
    # Start at the initial point
    x = x0
    y = y0
    
    # Draw the line
    for _ in range(int(steps) + 1):
        pygame.draw.circle(window, WHITE, (int(round(x)), int(round(y))), 1)
        x += x_increment
        y += y_increment

def main():
    # Set up initial and end points
    x0, y0 = 100, 100
    x1, y1 = 700, 500
    
    # Fill the background
    window.fill(BLACK)
    
    # Draw the line using DDA algorithm
    dda_line(x0, y0, x1, y1)
    
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
