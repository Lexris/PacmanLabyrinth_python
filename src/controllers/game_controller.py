import threading
import pyautogui

from src.environment.pacman import Pacman
from src.model.intelligence.agent import Agent
import time


class GameController:
    def __init__(self, window_height, window_width):
        self._game = Pacman(window_height, window_width)
        self._agent = Agent(self._game)

    def __run_pacman_solution(self):
        """
        Secondary thread for the agent, activates when getting a 'q' event in the game and exists the program when getting
        an 'Escape' event.
        Time polling is used in other to reduce the resources used by the active waiting, since we need the agent to start
        only when/if it is initiated through the game event and the same goes for exiting the program.
        """
        while True:
            if self._game.exit is True:
                exit(2)
            elif self._game.agent_state:
                pyautogui.click(x=self._game.screen_size[0] / 2, y=self._game.screen_size[1] / 2)
                solution = self._agent.astar_search()
                for move in solution:
                    pyautogui.press(move)
                    if self._game.exit is True:
                        exit(2)
                    if not self._game.agent_state:
                        break
                self._game.agent_state = False
            time.sleep(0.25)

    def launch_game(self):
        """
        Create secondary thread for agent, since the main one will be used by tkinter in order to display the GUI.
        """
        agent_thread = threading.Thread(target=self.__run_pacman_solution)
        agent_thread.start()
        self._game.launch_game()
