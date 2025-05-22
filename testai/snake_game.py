import tkinter as tk
from tkinter import messagebox
import random


class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.window.resizable(False, False)

        # Game constants
        self.GAME_WIDTH = 700
        self.GAME_HEIGHT = 500
        self.SPEED = 100
        self.SPACE_SIZE = 20
        self.BODY_PARTS = 3
        self.SNAKE_COLOR = "#00FF00"
        self.FOOD_COLOR = "#FF0000"
        self.BACKGROUND_COLOR = "#000000"

        # Game variables
        self.score = 0
        self.direction = "right"
        self.snake_positions = []

        # Create score label
        self.label = tk.Label(
            self.window, text=f"Score: {self.score}", font=("consolas", 20)
        )
        self.label.pack()

        # Create game canvas
        self.canvas = tk.Canvas(
            self.window,
            bg=self.BACKGROUND_COLOR,
            height=self.GAME_HEIGHT,
            width=self.GAME_WIDTH,
        )
        self.canvas.pack()

        # Center window
        self.window.update()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = int((screen_width / 2) - (self.GAME_WIDTH / 2))
        y = int((screen_height / 2) - (self.GAME_HEIGHT / 2))
        self.window.geometry(f"{self.GAME_WIDTH}x{self.GAME_HEIGHT+30}+{x}+{y}")

        # Bind keys
        self.window.bind("<Left>", lambda event: self.change_direction("left"))
        self.window.bind("<Right>", lambda event: self.change_direction("right"))
        self.window.bind("<Up>", lambda event: self.change_direction("up"))
        self.window.bind("<Down>", lambda event: self.change_direction("down"))

        # Initialize game
        self.init_game()

    def init_game(self):
        # Create snake
        for i in range(self.BODY_PARTS):
            x = self.SPACE_SIZE * (self.BODY_PARTS - i)
            y = self.SPACE_SIZE
            self.snake_positions.append([x, y])

        # Create initial food
        self.spawn_food()

        # Start game
        self.next_turn()

    def spawn_food(self):
        while True:
            x = (
                random.randint(
                    0, (self.GAME_WIDTH - self.SPACE_SIZE) // self.SPACE_SIZE
                )
                * self.SPACE_SIZE
            )
            y = (
                random.randint(
                    0, (self.GAME_HEIGHT - self.SPACE_SIZE) // self.SPACE_SIZE
                )
                * self.SPACE_SIZE
            )

            # Check if food spawns on snake
            if [x, y] not in self.snake_positions:
                self.food_pos = [x, y]
                break

    def next_turn(self):
        # Get current head position
        head = self.snake_positions[0].copy()

        # Move head based on direction
        if self.direction == "left":
            head[0] -= self.SPACE_SIZE
        elif self.direction == "right":
            head[0] += self.SPACE_SIZE
        elif self.direction == "up":
            head[1] -= self.SPACE_SIZE
        elif self.direction == "down":
            head[1] += self.SPACE_SIZE

        # Insert new head
        self.snake_positions.insert(0, head)

        # Check if food eaten
        if head == self.food_pos:
            self.score += 1
            self.label.config(text=f"Score: {self.score}")
            self.spawn_food()
        else:
            self.snake_positions.pop()

        # Check for collision
        if self.check_collision():
            self.game_over()
        else:
            # Draw everything
            self.draw_game()
            # Schedule next turn
            self.window.after(self.SPEED, self.next_turn)

    def check_collision(self):
        head = self.snake_positions[0]

        # Check wall collision
        if (
            head[0] < 0
            or head[0] >= self.GAME_WIDTH
            or head[1] < 0
            or head[1] >= self.GAME_HEIGHT
        ):
            return True

        # Check self collision
        if head in self.snake_positions[1:]:
            return True

        return False

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            self.GAME_WIDTH / 2,
            self.GAME_HEIGHT / 2,
            font=("consolas", 70),
            text="GAME OVER",
            fill="red",
        )

        # Show restart message
        if messagebox.askokcancel(
            "Game Over", f"Your score: {self.score}\nWould you like to restart?"
        ):
            # Reset game state
            self.score = 0
            self.direction = "right"
            self.snake_positions = []
            self.label.config(text=f"Score: {self.score}")
            self.canvas.delete("all")
            self.init_game()
        else:
            self.window.destroy()

    def change_direction(self, new_direction):
        # Prevent 180 degree turns
        if (
            new_direction == "left"
            and self.direction != "right"
            or new_direction == "right"
            and self.direction != "left"
            or new_direction == "up"
            and self.direction != "down"
            or new_direction == "down"
            and self.direction != "up"
        ):
            self.direction = new_direction

    def draw_game(self):
        # Clear canvas
        self.canvas.delete("all")

        # Draw snake
        for pos in self.snake_positions:
            self.canvas.create_rectangle(
                pos[0],
                pos[1],
                pos[0] + self.SPACE_SIZE,
                pos[1] + self.SPACE_SIZE,
                fill=self.SNAKE_COLOR,
                outline="#003300",
            )

        # Draw food
        self.canvas.create_oval(
            self.food_pos[0],
            self.food_pos[1],
            self.food_pos[0] + self.SPACE_SIZE,
            self.food_pos[1] + self.SPACE_SIZE,
            fill=self.FOOD_COLOR,
            outline="#550000",
        )


if __name__ == "__main__":
    game = SnakeGame()
    game.window.mainloop()
