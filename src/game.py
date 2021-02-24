import time
import tkinter
from PIL import Image, ImageTk

from src.utils.constants import *


class Game:
    def __init__(self, window_height, window_width):
        # init window and make it resizable
        self.window = tkinter.Tk()
        self.window.title(WINDOW_TITLE)
        self.window.geometry('+%d+%d' % (
            self.window.winfo_screenwidth() / 2 - window_width / 2,
            self.window.winfo_screenheight() / 2 - window_height / 2))
        self.window.iconphoto(False, tkinter.PhotoImage(file=WINDOW_LOGO_IMAGE_PATH))
        self.window.resizable(False, False)
        # init canvas and attach grid drawing function
        self.canvas = tkinter.Canvas(self.window, height=window_height, width=window_width, bg='#262624')
        self.canvas.pack(fill=tkinter.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.setup_board)
        self.canvas.bind('<Key>', self.draw_pacman)
        self.canvas.bind('<1>', lambda event: self.canvas.focus_set())
        # load pacman graphics
        self.pacman_image = Image.open(PACMAN_IMAGE_PATH).resize((40, 40), Image.ANTIALIAS)
        self.pacman_tkinter_image = ImageTk.PhotoImage(self.pacman_image)
        self.pacman_angle = 0
        self.pacman_position = (28, 28)
        # load pacman food graphics
        self.pacman_food_image = Image.open(PACMAN_FOOD_IMAGE_PATH).resize((40, 40), Image.ANTIALIAS)
        self.pacman_food_tkinter_image = ImageTk.PhotoImage(self.pacman_food_image)
        # pacman game state
        self.is_over = False
        self.timer = time.time()
        self.setup_board()

    def draw_grid(self, height, width):
        """
        Draw the grid
        :param height: window height
        :param width: window width
        """
        self.canvas.delete('grid')
        for i in range(6, height, 44):
            self.canvas.create_line(i, 6, i, height - 1, fill='yellow', tag='grid')
        for i in range(6, width, 44):
            self.canvas.create_line(6, i, width - 1, i, fill='yellow', tag='grid')

    def draw_obstacles(self):
        """
        Draw the obstacles
        """
        self.canvas.delete('obstacles')
        for i in range(0, 18):
            for j in range(0, 18):
                if PACMAN_BOARD_OBSTACLES_800x800[j][i] == 1:
                    self.canvas.create_rectangle(6 + 44 * i, 6 + 44 * j,
                                                 6 + 44 * (i + 1), 6 + 44 * (j + 1),
                                                 fill='yellow', tag='obstacles')

    def set_next_pacman_position(self, move):
        rotation_angle = PACMAN_ORIENTATIONS.get(move).get(self.pacman_angle)
        self.pacman_image = self.pacman_image.rotate(rotation_angle)
        self.pacman_angle += rotation_angle
        new_x = self.pacman_position[0] + PACMAN_MOVEMENTS[move][0]
        new_y = self.pacman_position[1] + PACMAN_MOVEMENTS[move][1]

        if new_x < 28:
            new_x = 28
        elif new_x > self.window.winfo_width() - 28:
            new_x = self.window.winfo_width() - 28
        if new_y < 28:
            new_y = 28
        elif new_y > self.window.winfo_height() - 28:
            new_y = self.window.winfo_height() - 28

        if PACMAN_BOARD_OBSTACLES_800x800[int((new_y - 28) / 44)][int((new_x - 28) / 44)] == 0:
            self.pacman_position = (new_x, new_y)
            print(str(int((new_y - 28) / 44)), str(int((new_x - 28) / 44)))

    def refresh_pacman(self):
        self.canvas.delete('pacman')
        self.pacman_tkinter_image = ImageTk.PhotoImage(self.pacman_image)
        self.canvas.move(self.pacman_tkinter_image, self.pacman_position[0], self.pacman_position[1])
        self.canvas.create_image(self.pacman_position[0], self.pacman_position[1], image=self.pacman_tkinter_image,
                                 tag='pacman')

    def check_game_over(self):
        if self.pacman_position[0] == self.window.winfo_width() - 1 * 44 - 28 and self.pacman_position[1] == 28 + 2 * 44:
            self.terminate_game()

    def get_pacman_board_coords(self):
        return int((self.pacman_position[1] - 28) / 44), int((self.pacman_position[0] - 28) / 44)

    def draw_pacman(self, event=None):
        """
        Draws pacman according to the events
        :param event: canvas event
        """
        if event:
            if event.char in PACMAN_ORIENTATION_KEYS:
                self.set_next_pacman_position(event.char)
        self.refresh_pacman()
        self.check_game_over()

    def draw_pacman_food(self):
        """
        Draw the pacman food(objective)
        """
        self.canvas.delete('pacman_food')
        self.canvas.create_image(self.window.winfo_width() - 1 * 44 - 28, 28 + 2 * 44,
                                 image=self.pacman_food_tkinter_image, tag='pacman_food')

    def setup_board(self, event=None):
        """
        Setup the board for the labyrinth game: draw the grid, draw the obstacles, draw pacman and pacman food,
        """
        self.canvas.config(height=event.height - 4, width=event.width - 4)
        self.draw_grid(height=event.height - 4, width=event.width - 4)
        self.draw_obstacles()
        self.draw_pacman()
        self.draw_pacman_food()

    def start_game(self):
        """
        Launch the game
        """
        self.window.mainloop()

    def terminate_game(self):
        """
        Terminate the game
        """
        self.timer = (time.time() - self.timer)
        print("Congratulations, you won in just " + str(self.timer))
