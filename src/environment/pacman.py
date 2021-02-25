import time
import tkinter
from PIL import Image, ImageTk

from src.utils.constants import *


class Pacman:
    def __init__(self, window_height, window_width):
        # init window, set screen position, change window icon, disable resize
        self.window = tkinter.Tk()
        self.window.title(WINDOW_TITLE)
        window_coord_x = self.window.winfo_screenwidth() / 2 - window_width / 2
        window_coord_y = self.window.winfo_screenheight() / 2 - window_height / 2
        self.window.geometry('+%d+%d' % (window_coord_x, window_coord_y))
        self.window.iconphoto(False, tkinter.PhotoImage(file=WINDOW_LOGO_IMAGE_PATH))
        self.window.resizable(False, False)

        # init canvas and bind board initialization and keyboard pacman movement
        self.canvas = tkinter.Canvas(self.window, height=window_height, width=window_width, bg=BOARD_BACKGROUND_COLOR)
        self.canvas.pack(fill=tkinter.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.setup_board)
        self.canvas.bind('<Key>', self.draw_pacman)
        self.canvas.bind('<1>', lambda event: self.canvas.focus_set())

        # load pacman graphics
        self.pacman_image = Image.open(PACMAN_IMAGE_PATH).resize((40, 40), Image.ANTIALIAS)
        self.pacman_tkinter_image = ImageTk.PhotoImage(self.pacman_image)
        self.pacman_angle = 0
        self.pacman_window_coords = PACMAN_INITIAL_WINDOW_COORDS
        self.pacman_board_coords = (0, 0)

        # load pacman food graphics
        self.pacman_food_image = Image.open(PACMAN_FOOD_IMAGE_PATH).resize((40, 40), Image.ANTIALIAS)
        self.pacman_food_tkinter_image = ImageTk.PhotoImage(self.pacman_food_image)
        self.pacman_food_board_coords = PACMAN_FOOD_BOARD_COORDS

        # pacman game state
        self.board = PACMAN_BOARD_OBSTACLES_800x800
        self.is_game_over = False
        self.timer = time.time()

    def draw_grid(self, height, width):
        """
        Draw the grid
        :param height: window height
        :param width: window width
        """
        self.canvas.delete('grid')
        for i in range(6, height, 44):
            self.canvas.create_line(i, 6, i, height - 1, fill=GRID_LINES_COLOR, tag='grid')
        for i in range(6, width, 44):
            self.canvas.create_line(6, i, width - 1, i, fill=GRID_LINES_COLOR, tag='grid')

    def draw_obstacles(self):
        """
        Draw the obstacles where the labyrinth matrix's value is 1
        """
        self.canvas.delete('obstacles')
        for i in range(0, 18):
            for j in range(0, 18):
                if self.board[j][i] == 1:
                    self.canvas.create_rectangle(6 + 44 * i, 6 + 44 * j,
                                                 6 + 44 * (i + 1), 6 + 44 * (j + 1),
                                                 fill='yellow', tag='obstacles')

    def get_next_pacman_position(self, move):
        """
        Calculate next pacman orientation and position on the board
        :param move: indicates the direction of intended movement
        """
        # rotate the pacman image as to simulate the orientation of the character
        rotation_angle = PACMAN_ORIENTATIONS.get(move).get(self.pacman_angle)
        self.pacman_image = self.pacman_image.rotate(rotation_angle)
        self.pacman_angle += rotation_angle

        # get new pacman position
        new_x = self.pacman_window_coords[0] + PACMAN_MOVEMENTS[move][0]
        new_y = self.pacman_window_coords[1] + PACMAN_MOVEMENTS[move][1]

        # check if position indicated by move is within the boundaries of the board
        if new_x < 28:
            new_x = 28
        elif new_x > self.window.winfo_width() - 28:
            new_x = self.window.winfo_width() - 28
        if new_y < 28:
            new_y = 28
        elif new_y > self.window.winfo_height() - 28:
            new_y = self.window.winfo_height() - 28

        # check if new position is an obstacle, if not return next pacman position(window coords and board coords)
        new_board_coord_x = int((new_y - 28) / 44)
        new_board_coord_y = int((new_x - 28) / 44)
        if self.board[new_board_coord_x][new_board_coord_y] == 0:
            return (new_x, new_y), (new_board_coord_x, new_board_coord_y)

    def refresh_pacman(self):
        """
        Redraw pacman with the new orientation and position
        """
        self.canvas.delete('pacman')
        self.pacman_tkinter_image = ImageTk.PhotoImage(self.pacman_image)
        self.canvas.move(self.pacman_tkinter_image, self.pacman_window_coords[0], self.pacman_window_coords[1])
        self.canvas.create_image(self.pacman_window_coords[0], self.pacman_window_coords[1], image=self.pacman_tkinter_image,
                                 tag='pacman')

    def is_goal_state(self):
        """
        Check if pacman has reached the food
        :return: True if goal has been achieved, False otherwise
        """
        if self.pacman_board_coords == self.pacman_food_board_coords:
            return True
        else:
            return False

    def draw_pacman(self, event=None):
        """
        Draws pacman according to the events
        :param event: canvas event
        """
        if event:
            if event.char in PACMAN_CONTROLS:
                self.pacman_window_coords, self.pacman_board_coords = self.get_next_pacman_position(event.char)
        self.refresh_pacman()
        if self.is_goal_state():
            self.terminate_game()

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
