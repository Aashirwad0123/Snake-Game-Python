import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20
SPEED = 10

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the snake and food
snake = [(200, 200), (220, 200), (240, 200)]
food = (400, 300)

# Set up the direction
direction = 'right'

# Function to generate obstacles
def generate_obstacles(snake, food, num_obstacles=5):
    obstacles = []
    while len(obstacles) < num_obstacles:
        pos = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
               random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
        if pos not in snake and pos != food:
            obstacles.append(pos)
    return obstacles

# Generate initial obstacles
obstacles = generate_obstacles(snake, food)

# Set up snake color
snake_color = GREEN

# Function to show message on screen
def show_message(message, color, y_displace=0, size='large'):
    font = pygame.font.Font(None, 75 if size == 'large' else 36)
    text = font.render(message, True, color)
    rect = text.get_rect()
    rect.center = (WIDTH // 2, HEIGHT // 2 + y_displace)
    screen.blit(text, rect)
    pygame.display.flip()

# Main menu
show_message('Press any key to start', WHITE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            break
    else:
        continue
    break

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != 'down':
                direction = 'up'
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != 'up':
                direction = 'down'
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != 'right':
                direction = 'left'
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != 'left':
                direction = 'right'
            # Change snake color
            elif event.key == pygame.K_1:
                snake_color = GREEN
            elif event.key == pygame.K_2:
                snake_color = BLUE
            elif event.key == pygame.K_3:
                snake_color = YELLOW

    # Move the snake
    head = snake[-1]
    if direction == 'up':
        new_head = (head[0], head[1] - BLOCK_SIZE)
    elif direction == 'down':
        new_head = (head[0], head[1] + BLOCK_SIZE)
    elif direction == 'left':
        new_head = (head[0] - BLOCK_SIZE, head[1])
    elif direction == 'right':
        new_head = (head[0] + BLOCK_SIZE, head[1])
    snake.append(new_head)

    # Check for collision with food
    if snake[-1] == food:
        food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
        # Regenerate obstacles to avoid overlap with new food position
        obstacles = generate_obstacles(snake, food)
    else:
        snake.pop(0)

    # Check for collision with self, edge, or obstacles
    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
            snake[-1][1] < 0 or snake[-1][1] >= HEIGHT or
            snake[-1] in snake[:-1] or
            snake[-1] in obstacles):
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)
    for pos in snake:
        pygame.draw.rect(screen, snake_color, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    for obs in obstacles:
        pygame.draw.rect(screen, WHITE, (obs[0], obs[1], BLOCK_SIZE, BLOCK_SIZE))
    text = font.render(f'Score: {len(snake)}', True, WHITE)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(SPEED)
