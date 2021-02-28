from PIL import Image, ImageTk

from src.environment.base_game import BaseGame
from src.utils.constants import *


class Pacman(BaseGame):
    def __init__(self, window_height, window_width):
        # init base game class(common game features)
        super().__init__(window_height, window_width)

        # bind specific pacman functionalities to canvas
        self.canvas.bind('<Configure>', self.setup_board)
        self.canvas.bind('<Key>', self.refresh_pacman)
        self.canvas.bind('<q>', self.toggle_agent)

        # load pacman graphics
        self.pacman_image = Image\
            .open(PACMAN_IMAGE_PATH)\
            .resize((IMAGE_RESIZE_FACTOR, IMAGE_RESIZE_FACTOR), Image.ANTIALIAS)
        self.pacman_tkinter_image = ImageTk.PhotoImage(self.pacman_image)
        self.pacman_angle = 0
        self.pacman_window_coords = PACMAN_INITIAL_WINDOW_COORDS
        self.pacman_board_coords = (0, 0)

        # load pacman food graphics
        self.pacman_food_image = Image\
            .open(PACMAN_FOOD_IMAGE_PATH)\
            .resize((IMAGE_RESIZE_FACTOR, IMAGE_RESIZE_FACTOR), Image.ANTIALIAS)
        self.pacman_food_tkinter_image = ImageTk.PhotoImage(self.pacman_food_image)
        self.pacman_food_board_coords = PACMAN_FOOD_BOARD_COORDS

    def draw_grid(self, height, width):
        """
        Draw the grid, with lines every 44px(leaving 6px margin with the main window)
        :param height: window height
        :param width: window width
        """
        self.canvas.delete('grid')
        for i in range(PACMAN_BOARD_800x800_WINDOW_MARGIN, height, PACMAN_BOARD_800x800_SQUARE_SIDE_LENGTH):
            self.canvas.create_line(
                # coords for starting and ending point of the line x1, y1, x2 ,y2
                i, PACMAN_BOARD_800x800_WINDOW_MARGIN, i, height - 1,
                fill=GRID_COLOR,
                tag=GRID_TAG
            )
        for i in range(PACMAN_BOARD_800x800_WINDOW_MARGIN, width, PACMAN_BOARD_800x800_SQUARE_SIDE_LENGTH):
            self.canvas.create_line(
                # coords for starting and ending point of the line x1, y1, x2 ,y2
                PACMAN_BOARD_800x800_WINDOW_MARGIN, i, width - 1, i,
                fill=GRID_COLOR,
                tag=GRID_TAG
            )

    def draw_obstacles(self):
        """
        Draw the obstacles where the labyrinth matrix's value is 1
        """
        self.canvas.delete(OBSTACLES_TAG)
        for i in range(0, PACMAN_BOARD_800x800_SIDE_SQUARES_NUMBER):
            for j in range(0, PACMAN_BOARD_800x800_SIDE_SQUARES_NUMBER):
                if self.board[j][i] == 1:
                    self.canvas.create_rectangle(
                        PACMAN_BOARD_800x800_WINDOW_MARGIN + PACMAN_BOARD_800x800_SQUARE_SIDE_LENGTH * i,
                        PACMAN_BOARD_800x800_WINDOW_MARGIN + PACMAN_BOARD_800x800_SQUARE_SIDE_LENGTH * j,
                        PACMAN_BOARD_800x800_WINDOW_MARGIN + PACMAN_BOARD_800x800_SQUARE_SIDE_LENGTH * (i + 1),
                        PACMAN_BOARD_800x800_WINDOW_MARGIN + PACMAN_BOARD_800x800_SQUARE_SIDE_LENGTH * (j + 1),
                        fill=OBSTACLES_COLOR,
                        tag=OBSTACLES_TAG
                    )

    def draw_pacman(self):
        """
        Draw pacman
        """
        self.canvas.delete(PACMAN_TAG)
        self.pacman_tkinter_image = ImageTk.PhotoImage(self.pacman_image)
        self.canvas.move(self.pacman_tkinter_image, self.pacman_window_coords[0], self.pacman_window_coords[1])
        self.canvas.create_image(
            self.pacman_window_coords[0],
            self.pacman_window_coords[1],
            image=self.pacman_tkinter_image,
            tag=PACMAN_TAG
        )

    def draw_pacman_food(self):
        """
        Draw the pacman food(objective)
        """
        self.canvas.delete(PACMAN_FOOD_TAG)
        self.canvas.create_image(
            self.window.winfo_width() - 1 * PACMAN_BOARD_800x800_SQUARE_SIDE_LENGTH - FOOD_MARGIN,
            FOOD_MARGIN + 2 * PACMAN_BOARD_800x800_SQUARE_SIDE_LENGTH,
            image=self.pacman_food_tkinter_image,
            tag=PACMAN_FOOD_TAG
        )

    def setup_board(self, event=None):
        """
        Setup the board for the labyrinth game: draw the grid, draw the obstacles, draw pacman and pacman food
        :param event: the only event that should trigger this function is the initialization of the canvas(which
        only happens once throughout the lifespan of the process)
        """
        self.canvas.config(height=event.height - 4, width=event.width - 4)
        self.draw_grid(height=event.height - 4, width=event.width - 4)
        self.draw_obstacles()
        self.draw_pacman()
        self.draw_pacman_food()

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
        if new_x < PACMAN_MARGIN:
            new_x = PACMAN_MARGIN
        elif new_x > self.window.winfo_width() - PACMAN_MARGIN:
            new_x = self.window.winfo_width() - PACMAN_MARGIN
        if new_y < PACMAN_MARGIN:
            new_y = PACMAN_MARGIN
        elif new_y > self.window.winfo_height() - PACMAN_MARGIN:
            new_y = self.window.winfo_height() - PACMAN_MARGIN

        # check if new position is an obstacle, if not return next pacman position(window coords and board coords)
        new_board_coord_x = int((new_y - PACMAN_MARGIN) / PACMAN_BOARD_800x800_SQUARE_SIDE_LENGTH)
        new_board_coord_y = int((new_x - PACMAN_MARGIN) / PACMAN_BOARD_800x800_SQUARE_SIDE_LENGTH)
        if self.board[new_board_coord_x][new_board_coord_y] == 0:
            self.cost += 1
            return (new_x, new_y), (new_board_coord_x, new_board_coord_y)
        else:
            return (self.pacman_window_coords[0], self.pacman_window_coords[1]), \
                   (self.pacman_board_coords[0], self.pacman_board_coords[1])

    def refresh_pacman(self, event=None):
        """
        Refresh pacman according to the events
        :param event: changes will be made to the game state if and only if the event is triggered by the defined
        movement keys(see constants.py)
        """
        if not self.is_game_over:
            if event:
                if event.char in PACMAN_CONTROLS:
                    self.pacman_window_coords, self.pacman_board_coords = self.get_next_pacman_position(event.char)
                    self.draw_pacman()
            if self.is_goal_state():
                self.terminate_game()

    def is_goal_state(self, state=None):
        """
        Check if pacman has reached the food.
        :param state: state to be checked; if None, current state of the game will be checked
        :return: True if state is goal state, False otherwise
        """
        if state:
            return state == self.pacman_food_board_coords
        else:
            return self.pacman_board_coords == self.pacman_food_board_coords
