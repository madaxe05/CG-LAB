import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Midpoint Circle Drawing Algorithm")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_circle_points(x_center, y_center, x, y):
    # Draw points in all eight octants
    points = [
        (x_center + x, y_center + y),
        (x_center - x, y_center + y),
        (x_center + x, y_center - y),
        (x_center - x, y_center - y),
        (x_center + y, y_center + x),
        (x_center - y, y_center + x),
        (x_center + y, y_center - x),
        (x_center - y, y_center - x)
    ]
    
    for point in points:
        pygame.draw.circle(window, WHITE, point, 1)

def midpoint_circle(x_center, y_center, radius):
    x = 0
    y = radius
    d = 1 - radius
    
    draw_circle_points(x_center, y_center, x, y)
    
    while x < y:
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
        draw_circle_points(x_center, y_center, x, y)

def main():
    # Set up center and radius of the circle
    x_center, y_center = 400, 300
    radius = 100
    
    # Fill the background
    window.fill(BLACK)
    
    # Draw the circle using the Midpoint Circle Algorithm
    midpoint_circle(x_center, y_center, radius)
    
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
