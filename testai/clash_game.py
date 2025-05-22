import pygame
import sys
import random
import math
from pygame.locals import *

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Clash Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)
GRAY = (128, 128, 128)
DARK_GREEN = (0, 100, 0)

# Game variables
clock = pygame.time.Clock()
FPS = 60

# Font
font = pygame.font.SysFont("Arial", 20)
large_font = pygame.font.SysFont("Arial", 32)


class Building:
    def __init__(self, x, y, width, height, building_type, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = building_type
        self.max_health = health
        self.health = health
        self.color = self.get_color()
        self.resource_timer = 0
        self.resource_interval = 3000  # milliseconds

    def get_color(self):
        if self.type == "town_hall":
            return PURPLE
        elif self.type == "gold_mine":
            return GOLD
        elif self.type == "elixir_collector":
            return PURPLE
        elif self.type == "cannon":
            return GRAY
        elif self.type == "wall":
            return BROWN
        else:
            return BLACK

    def draw(self, surface):
        # Draw building
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

        # Draw health bar
        health_ratio = self.health / self.max_health
        health_bar_width = self.width * health_ratio
        pygame.draw.rect(surface, RED, (self.x, self.y - 10, self.width, 5))
        pygame.draw.rect(surface, GREEN, (self.x, self.y - 10, health_bar_width, 5))

        # Draw label
        label = font.render(self.type.replace("_", " ").title(), True, BLACK)
        surface.blit(label, (self.x, self.y + self.height + 5))

    def collect_resources(self, game):
        if self.type in ["gold_mine", "elixir_collector"]:
            current_time = pygame.time.get_ticks()
            if current_time - self.resource_timer >= self.resource_interval:
                if self.type == "gold_mine":
                    game.gold += 10
                else:
                    game.elixir += 10
                self.resource_timer = current_time
                return True
        return False

    def is_clicked(self, pos):
        x, y = pos
        return (
            self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height
        )


class Troop:
    def __init__(self, x, y, troop_type):
        self.x = x
        self.y = y
        self.type = troop_type
        self.radius = 10
        self.speed = 1
        self.health = 100
        self.max_health = 100
        self.damage = 10
        self.attack_range = 50
        self.attack_cooldown = 1000  # milliseconds
        self.last_attack = 0
        self.target = None

        if troop_type == "barbarian":
            self.color = RED
            self.damage = 15
        elif troop_type == "archer":
            self.color = BLUE
            self.attack_range = 100
            self.damage = 8
        elif troop_type == "giant":
            self.color = BROWN
            self.radius = 15
            self.health = 200
            self.max_health = 200
            self.damage = 20
            self.speed = 0.5

    def draw(self, surface):
        # Draw troop
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

        # Draw health bar
        health_ratio = self.health / self.max_health
        health_bar_width = self.radius * 2 * health_ratio
        pygame.draw.rect(
            surface,
            RED,
            (self.x - self.radius, self.y - self.radius - 10, self.radius * 2, 3),
        )
        pygame.draw.rect(
            surface,
            GREEN,
            (self.x - self.radius, self.y - self.radius - 10, health_bar_width, 3),
        )

    def move_towards(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance > 0:
            dx = dx / distance
            dy = dy / distance
            self.x += dx * self.speed
            self.y += dy * self.speed

    def find_target(self, buildings):
        closest_building = None
        closest_distance = float("inf")

        for building in buildings:
            if building.health <= 0:
                continue

            # Calculate distance to building center
            building_center_x = building.x + building.width / 2
            building_center_y = building.y + building.height / 2
            dx = building_center_x - self.x
            dy = building_center_y - self.y
            distance = math.sqrt(dx**2 + dy**2)

            if distance < closest_distance:
                closest_distance = distance
                closest_building = building

        return closest_building, closest_distance

    def attack(self, buildings):
        current_time = pygame.time.get_ticks()

        # Find target if we don't have one or if current target is destroyed
        if self.target is None or self.target.health <= 0:
            self.target, distance = self.find_target(buildings)

        if self.target:
            # Calculate distance to target
            target_center_x = self.target.x + self.target.width / 2
            target_center_y = self.target.y + self.target.height / 2
            dx = target_center_x - self.x
            dy = target_center_y - self.y
            distance = math.sqrt(dx**2 + dy**2)

            # If in range, attack
            if distance <= self.attack_range:
                if current_time - self.last_attack >= self.attack_cooldown:
                    self.target.health -= self.damage
                    self.last_attack = current_time
                    if self.target.health <= 0:
                        self.target = None
            else:
                # Move towards target
                self.move_towards(target_center_x, target_center_y)


class Game:
    def __init__(self):
        self.buildings = []
        self.troops = []
        self.gold = 100
        self.elixir = 100
        self.selected_building = None
        self.selected_troop = None
        self.game_state = "building"  # "building" or "attacking"
        self.victory = False
        self.defeat = False

        # Initialize base with some buildings
        self.initialize_base()

    def initialize_base(self):
        # Town Hall
        self.buildings.append(Building(350, 250, 80, 80, "town_hall", 500))

        # Resource buildings
        self.buildings.append(Building(200, 200, 50, 50, "gold_mine", 200))
        self.buildings.append(Building(500, 200, 50, 50, "elixir_collector", 200))

        # Defenses
        self.buildings.append(Building(300, 350, 40, 40, "cannon", 300))
        self.buildings.append(Building(450, 350, 40, 40, "cannon", 300))

        # Walls
        for i in range(5):
            self.buildings.append(Building(250 + i * 60, 150, 20, 20, "wall", 100))
            self.buildings.append(Building(250 + i * 60, 400, 20, 20, "wall", 100))
        for i in range(4):
            self.buildings.append(Building(230, 170 + i * 60, 20, 20, "wall", 100))
            self.buildings.append(Building(530, 170 + i * 60, 20, 20, "wall", 100))

    def draw(self, surface):
        # Draw grass background
        surface.fill(DARK_GREEN)

        # Draw grid lines
        for x in range(0, SCREEN_WIDTH, 50):
            pygame.draw.line(surface, GREEN, (x, 0), (x, SCREEN_HEIGHT), 1)
        for y in range(0, SCREEN_HEIGHT, 50):
            pygame.draw.line(surface, GREEN, (0, y), (SCREEN_WIDTH, y), 1)

        # Draw buildings
        for building in self.buildings:
            if building.health > 0:
                building.draw(surface)

        # Draw troops
        for troop in self.troops:
            if troop.health > 0:
                troop.draw(surface)

        # Draw resources
        gold_text = font.render(f"Gold: {self.gold}", True, GOLD)
        elixir_text = font.render(f"Elixir: {self.elixir}", True, PURPLE)
        surface.blit(gold_text, (10, 10))
        surface.blit(elixir_text, (10, 40))

        # Draw game state
        state_text = font.render(f"Mode: {self.game_state.title()}", True, WHITE)
        surface.blit(state_text, (SCREEN_WIDTH - 150, 10))

        # Draw troop selection buttons in attack mode
        if self.game_state == "attacking":
            pygame.draw.rect(surface, RED, (SCREEN_WIDTH - 150, 50, 120, 30))
            pygame.draw.rect(surface, BLUE, (SCREEN_WIDTH - 150, 90, 120, 30))
            pygame.draw.rect(surface, BROWN, (SCREEN_WIDTH - 150, 130, 120, 30))

            barb_text = font.render("Barbarian (10)", True, WHITE)
            archer_text = font.render("Archer (15)", True, WHITE)
            giant_text = font.render("Giant (20)", True, WHITE)

            surface.blit(barb_text, (SCREEN_WIDTH - 145, 55))
            surface.blit(archer_text, (SCREEN_WIDTH - 145, 95))
            surface.blit(giant_text, (SCREEN_WIDTH - 145, 135))

        # Draw building selection buttons in building mode
        if self.game_state == "building":
            pygame.draw.rect(surface, GOLD, (SCREEN_WIDTH - 150, 50, 120, 30))
            pygame.draw.rect(surface, PURPLE, (SCREEN_WIDTH - 150, 90, 120, 30))
            pygame.draw.rect(surface, GRAY, (SCREEN_WIDTH - 150, 130, 120, 30))
            pygame.draw.rect(surface, BROWN, (SCREEN_WIDTH - 150, 170, 120, 30))

            mine_text = font.render("Gold Mine (50)", True, BLACK)
            collector_text = font.render("Elixir Coll (50)", True, BLACK)
            cannon_text = font.render("Cannon (80)", True, BLACK)
            wall_text = font.render("Wall (20)", True, BLACK)

            surface.blit(mine_text, (SCREEN_WIDTH - 145, 55))
            surface.blit(collector_text, (SCREEN_WIDTH - 145, 95))
            surface.blit(cannon_text, (SCREEN_WIDTH - 145, 135))
            surface.blit(wall_text, (SCREEN_WIDTH - 145, 175))

        # Draw switch mode button
        pygame.draw.rect(
            surface, WHITE, (SCREEN_WIDTH - 150, SCREEN_HEIGHT - 50, 120, 30)
        )
        switch_text = font.render("Switch Mode", True, BLACK)
        surface.blit(switch_text, (SCREEN_WIDTH - 145, SCREEN_HEIGHT - 45))

        # Draw victory/defeat message
        if self.victory:
            victory_text = large_font.render("VICTORY!", True, GOLD)
            surface.blit(
                victory_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 20)
            )
        elif self.defeat:
            defeat_text = large_font.render("DEFEAT!", True, RED)
            surface.blit(defeat_text, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 - 20))

    def handle_click(self, pos):
        x, y = pos

        # Check if switch mode button is clicked
        if (
            SCREEN_WIDTH - 150 <= x <= SCREEN_WIDTH - 30
            and SCREEN_HEIGHT - 50 <= y <= SCREEN_HEIGHT - 20
        ):
            self.game_state = (
                "attacking" if self.game_state == "building" else "building"
            )
            return

        # Handle building mode
        if self.game_state == "building":
            # Check if building selection buttons are clicked
            if SCREEN_WIDTH - 150 <= x <= SCREEN_WIDTH - 30:
                if 50 <= y <= 80 and self.gold >= 50:  # Gold Mine
                    self.selected_building = "gold_mine"
                    return
                elif 90 <= y <= 120 and self.elixir >= 50:  # Elixir Collector
                    self.selected_building = "elixir_collector"
                    return
                elif 130 <= y <= 160 and self.gold >= 80:  # Cannon
                    self.selected_building = "cannon"
                    return
                elif 170 <= y <= 200 and self.gold >= 20:  # Wall
                    self.selected_building = "wall"
                    return

            # Place selected building
            if self.selected_building:
                if self.selected_building == "gold_mine" and self.gold >= 50:
                    self.buildings.append(
                        Building(x - 25, y - 25, 50, 50, "gold_mine", 200)
                    )
                    self.gold -= 50
                elif self.selected_building == "elixir_collector" and self.elixir >= 50:
                    self.buildings.append(
                        Building(x - 25, y - 25, 50, 50, "elixir_collector", 200)
                    )
                    self.elixir -= 50
                elif self.selected_building == "cannon" and self.gold >= 80:
                    self.buildings.append(
                        Building(x - 20, y - 20, 40, 40, "cannon", 300)
                    )
                    self.gold -= 80
                elif self.selected_building == "wall" and self.gold >= 20:
                    self.buildings.append(Building(x - 10, y - 10, 20, 20, "wall", 100))
                    self.gold -= 20

                self.selected_building = None

        # Handle attacking mode
        elif self.game_state == "attacking":
            # Check if troop selection buttons are clicked
            if SCREEN_WIDTH - 150 <= x <= SCREEN_WIDTH - 30:
                if 50 <= y <= 80 and self.elixir >= 10:  # Barbarian
                    self.selected_troop = "barbarian"
                    self.elixir -= 10
                    return
                elif 90 <= y <= 120 and self.elixir >= 15:  # Archer
                    self.selected_troop = "archer"
                    self.elixir -= 15
                    return
                elif 130 <= y <= 160 and self.elixir >= 20:  # Giant
                    self.selected_troop = "giant"
                    self.elixir -= 20
                    return

            # Deploy selected troop
            if self.selected_troop:
                self.troops.append(Troop(x, y, self.selected_troop))
                self.selected_troop = None

    def update(self):
        # Collect resources from buildings
        for building in self.buildings:
            building.collect_resources(self)

        # Update troops
        for troop in self.troops:
            if troop.health > 0:
                troop.attack(self.buildings)

        # Check for victory/defeat conditions
        town_hall_destroyed = True
        all_buildings_destroyed = True
        all_troops_dead = True

        for building in self.buildings:
            if building.type == "town_hall" and building.health > 0:
                town_hall_destroyed = False
            if building.health > 0:
                all_buildings_destroyed = False

        for troop in self.troops:
            if troop.health > 0:
                all_troops_dead = False

        if town_hall_destroyed or all_buildings_destroyed:
            self.victory = True

        if all_troops_dead and self.troops and self.game_state == "attacking":
            self.defeat = True


def main():
    game = Game()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    game.handle_click(event.pos)

        game.update()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
