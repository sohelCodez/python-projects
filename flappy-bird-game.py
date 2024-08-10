import tkinter as tk
import random

class FlappyBird:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.bird = self.canvas.create_rectangle(50, 200, 70, 220, fill='yellow')
        self.pipe_upper = self.canvas.create_rectangle(400, 0, 420, 150, fill='green')
        self.pipe_lower = self.canvas.create_rectangle(400, 250, 420, 400, fill='green')

        self.score_label = tk.Label(master, text="Score: 0")
        self.score_label.pack()

        self.high_score_label = tk.Label(master, text="High Score: {}".format(self.get_high_score()))
        self.high_score_label.pack()

        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.new_game_button = tk.Button(master, text="New Game", command=self.new_game)
        self.new_game_button.pack()
        self.new_game_button.config(state=tk.DISABLED)

        self.game_over_text = None  # To store the reference to the game over text object

        self.y = 0
        self.score = 0
        self.high_score = self.get_high_score()
        self.game_over = False

        self.canvas.bind_all('<KeyPress-space>', self.jump)

    def start_game(self):
        self.start_button.config(state=tk.DISABLED)
        self.new_game_button.config(state=tk.NORMAL)
        self.canvas.focus_set()
        self.score = 0
        self.game_over = False
        self.move()
        # Remove game over text if it exists
        if self.game_over_text:
            self.canvas.delete(self.game_over_text)
            self.game_over_text = None

    def new_game(self):
        self.new_game_button.config(state=tk.DISABLED)
        self.start_game()
        # Reset bird position
        self.canvas.coords(self.bird, 50, 200, 70, 220)
        # Reset pipe positions
        self.canvas.coords(self.pipe_upper, 400, 0, 420, 150)
        self.canvas.coords(self.pipe_lower, 400, 250, 420, 400)
        # Reset game state
        self.y = 0
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.game_over = False

    def move(self):
        if not self.game_over:
            self.canvas.move(self.pipe_upper, -5, 0)
            self.canvas.move(self.pipe_lower, -5, 0)
            self.check_collision()
            if self.canvas.coords(self.pipe_upper)[2] < 0:
                self.canvas.move(self.pipe_upper, 420, 0)
                self.canvas.move(self.pipe_lower, 420, 0)
                self.score += 1
                self.score_label.config(text="Score: {}".format(self.score))
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.high_score_label.config(text="High Score: {}".format(self.high_score))
            self.canvas.move(self.bird, 0, self.y)
            self.y += 1
            self.master.after(20, self.move)
        else:
            self.start_button.config(state=tk.NORMAL)
            if self.score > self.high_score:
                self.save_high_score(self.score)
            if not self.game_over_text:
                self.game_over_text = self.canvas.create_text(200, 200, text="Game Over!", font=("Helvetica", 30))

    def jump(self, event):
        if not self.game_over:
            self.y = -10

    def check_collision(self):
        bird_coords = self.canvas.coords(self.bird)
        pipe_upper_coords = self.canvas.coords(self.pipe_upper)
        pipe_lower_coords = self.canvas.coords(self.pipe_lower)

        if (bird_coords[0] < pipe_upper_coords[2] and bird_coords[2] > pipe_upper_coords[0] and
                (bird_coords[1] < pipe_upper_coords[3] or bird_coords[3] > pipe_lower_coords[1])):
            self.game_over = True

    def save_high_score(self, score):
        with open("high_score.txt", "w") as file:
            file.write(str(score))

    def get_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

def main():
    root = tk.Tk()
    root.title("Flappy Bird")
    game = FlappyBird(root)
    root.mainloop()

if __name__ == "__main__":
    main()