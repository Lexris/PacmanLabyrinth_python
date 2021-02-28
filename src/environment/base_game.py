import time
import tkinter

from src.utils.constants import *


class BaseGame:
    def __init__(self, window_height, window_width):
        # init window, set screen position, change window icon, disable resize
        self.window = tkinter.Tk()
        self.window.title(WINDOW_TITLE)
        self.screen_size = (self.window.winfo_screenwidth(), self.window.winfo_screenheight())
        window_coord_x = self.screen_size[0] / 2 - window_width / 2
        window_coord_y = self.screen_size[1] / 2 - window_height / 2
        self.window.geometry('+%d+%d' % (window_coord_x, window_coord_y))
        self.window.iconphoto(False, tkinter.PhotoImage(file=WINDOW_LOGO_IMAGE_PATH))
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.exit_protocol)

        # init canvas and bind basic functionalities
        self.canvas = tkinter.Canvas(self.window, height=window_height, width=window_width, bg=BOARD_BACKGROUND_COLOR)
        self.canvas.pack(fill=tkinter.BOTH, expand=True)
        self.canvas.bind('<1>', lambda event: self.canvas.focus_set())
        self.canvas.bind('<Escape>', self.exit_protocol)

        # game state
        self.board = PACMAN_BOARD_800x800_OBSTACLES  # for the sake of decoupling agent.py from constants.py
        self.is_agent_active = False
        self.cost = 0
        self.is_game_over = False
        self.timer = time.time()
        self.exit = False

    def toggle_agent(self, event=None):
        self.is_agent_active = not self.is_agent_active

    def launch_game(self):
        """
        Launch the game
        """
        self.window.mainloop()

    def terminate_game(self):
        """
        Terminate the game
        """
        self.timer = (time.time() - self.timer)
        print("Congratulations, you won with a score of " + str(int(1 / self.timer * SCORE_NORMALIZATION_FACTOR)))
        if self.cost == SOLUTION_OPTIMAL_COST:
            print("Your solution is optimal, are you a robot?")
        self.is_game_over = True

    def exit_protocol(self, event=None):
        """
        Exit the program
        :param event: will be an "<Esc" event
        """
        self.window.destroy()
        self.exit = True
