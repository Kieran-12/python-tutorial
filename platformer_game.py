import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("7 Worlds Platformer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 120, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
GRAY = (128, 128, 128)
BROWN = (139, 69, 19)
DARK_GREEN = (0, 100, 0)
LIGHT_BLUE = (173, 216, 230)

# Game variables
clock = pygame.time.Clock()
FPS = 60
GRAVITY = 0.5
JUMP_STRENGTH = -12
PLAYER_SPEED = 5

# Font
font = pygame.font.SysFont("Arial", 24)
large_font = pygame.font.SysFont("Arial", 48)


# Load images (using simple shapes for now)
def create_player_image():
    surf = pygame.Surface((30, 50), pygame.SRCALPHA)
    pygame.draw.rect(surf, BLUE, (0, 0, 30, 50))
    pygame.draw.rect(surf, LIGHT_BLUE, (5, 5, 20, 20))  # Face
    return surf


def create_coin_image():
    surf = pygame.Surface((20, 20), pygame.SRCALPHA)
    pygame.draw.circle(surf, YELLOW, (10, 10), 10)
    return surf


def create_enemy_image():
    surf = pygame.Surface((40, 30), pygame.SRCALPHA)
    pygame.draw.rect(surf, RED, (0, 0, 40, 30))
    pygame.draw.rect(surf, (255, 100, 100), (5, 5, 30, 10))  # Eyes
    return surf


def create_goal_image():
    surf = pygame.Surface((50, 50), pygame.SRCALPHA)
    pygame.draw.rect(surf, GREEN, (0, 0, 50, 50))
