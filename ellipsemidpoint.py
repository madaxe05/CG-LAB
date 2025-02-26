import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Midpoint Ellipse Drawing Algorithm")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_ellipse_points(x_center, y_center, x, y):
    # Draw points in all four quadrants
    points = [
        (x_center + x, y_center + y),
        (x_center - x, y_center + y),
        (x_center + x, y_center - y),
        (x_center - x, y_center - y)
    ]
    
    for point in points:
        pygame.draw.circle(window, WHITE, point, 1)

def midpoint_ellipse(x_center, y_center, rx, ry):
    # Region 1
    x = 0
    y = ry
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y
    p1 = ry**2 - (rx**2 * ry) + (0.25 * rx**2)
    
    while dx < dy:
        draw_ellipse_points(x_center, y_center, x, y)
        x += 1
        dx += 2 * ry**2
        if p1 < 0:
            p1 += dx + ry**2
        else:
            y -= 1
            dy -= 2 * rx**2
            p1 += dx - dy + ry**2
    
    # Region 2
    p2 = (ry**2) * (x + 0.5)**2 + (rx**2) * (y - 1)**2 - (rx**2 * ry**2)
    
    while y >= 0:
        draw_ellipse_points(x_center, y_center, x, y)
        y -= 1
        dy -= 2 * rx**2
        if p2 > 0:
            p2 += rx**2 - dy
        else:
            x += 1
            dx += 2 * ry**2
            p2 += dx - dy + rx**2

def main():
    # Set up center and radii of the ellipse
    x_center, y_center = 400, 300
    rx, ry = 200, 100
    
    # Fill the background
    window.fill(BLACK)
    
    # Draw the ellipse using the Midpoint Ellipse Algorithm
    midpoint_ellipse(x_center, y_center, rx, ry)
    
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
