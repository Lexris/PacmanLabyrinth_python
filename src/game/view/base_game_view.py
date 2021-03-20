import time
import tkinter

from src.utils.constants import *
from src.game.model.utils.constants import *


class BaseGameView:
    def __init__(self, window_height, window_width, difficulty):
        # init window, set screen position, change window icon, disable resize
        self._window = tkinter.Tk()
        self._window.title(WINDOW_TITLE)
        self.screen_size = (self._window.winfo_screenwidth(), self._window.winfo_screenheight())
        window_coord_x = self.screen_size[0] / 2 - window_width / 2
        window_coord_y = self.screen_size[1] / 2 - window_height / 2
        self._window.geometry('+%d+%d' % (window_coord_x, window_coord_y))
        self._window.iconphoto(False, tkinter.PhotoImage(file=WINDOW_LOGO_IMAGE_PATH))
        self._window.resizable(False, False)
        self._window.protocol('WM_DELETE_WINDOW', self._exit_protocol)
        self._window.config(cursor='none')

        # init canvas and bind basic functionalities
        self._canvas = tkinter.Canvas(self._window, height=window_height, width=window_width, bg=BOARD_BACKGROUND_COLOR)
        self._canvas.pack(fill=tkinter.BOTH, expand=True)
        self._canvas.bind('<1>', lambda event: self._canvas.focus_set())
        self._canvas.bind('<Escape>', self._exit_protocol)

        # game state
        self._game_state = False
        self.board = PACMAN_BOARD_OBSTACLES[difficulty]  # for the sake of decoupling agent.py from constants.py
        self.agent_state = False
        self.cost = 0
        self.optimal_solution = SOLUTION_OPTIMAL_COST[difficulty]
        self.timer = time.time()
        self.exit = False

    def _toggle_agent(self, event=None):
        """
        Toggle search agent on/off
        :param event: function will only run for a <q> keypress
        """
        if event:
            self.agent_state = not self.agent_state

    def _terminate_game(self):
        """
        Terminate the game when the user wins, and calculate the score as a function of the time the user needed for
        game completion
        """
        self.timer = (time.time() - self.timer)
        print("Congratulations, you won with a score of " + str(int(1 / self.timer * SCORE_NORMALIZATION_FACTOR)))
        if self.cost == self.optimal_solution:
            print("Your solution is optimal, are you a robot?")
        self._game_state = True

    def _exit_protocol(self, event=None):
        """
        Exit the program
        :param event: will be an <Esc> event or None
        """
        self._window.destroy()
        self.exit = True

    def launch_game(self):
        """
        Launch the game
        """
        self._window.mainloop()
