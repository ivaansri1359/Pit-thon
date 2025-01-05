import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100

# Ball dimensions
BALL_SIZE = 20

# Default speed
speed = 10
ball_speed = 2


# Paddle positions
left_paddle = pygame.Rect(30, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball position and velocity
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_velocity = [ball_speed, ball_speed]

# Scores
left_score = 0
right_score = 0

# Font
font = pygame.font.Font(None, 74)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= speed
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += speed
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += speed

    # Ball movement
    ball.x += ball_velocity[0]
    ball.y += ball_velocity[1]

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_velocity[1] = -ball_velocity[1]

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_velocity[0] = -ball_velocity[0]

    

    # Ball out of bounds
    if ball.left <= 0:
        right_score += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_velocity = [ball_speed, ball_speed]
    if ball.right >= WIDTH:
        left_score += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_velocity = [-ball_speed, -ball_speed]

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    left_text = font.render(str(left_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(right_text, (WIDTH * 3 // 4, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()