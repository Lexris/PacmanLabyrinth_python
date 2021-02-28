import threading
import time

import pyautogui

from src.environment.pacman import Pacman
from src.intelligence.agent import Agent
from src.utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH


def run_pacman_solution(pacman_agent):
    """
    Secondary thread for the agent, activates when getting a 'q' event in the game and exists the program when getting
    an 'Escape' event.
    Time polling is used in other to reduce the resources used by the active waiting, since we need the agent to start
    only when/if it is initiated through the game event and the same goes for exiting the program.
    :param pacman_agent: Agent containing the logic for solving the search problem.
    """
    while True:
        if pacman_agent.game.exit is True:
            exit(2)
        elif pacman_agent.game.is_agent_active:
            pyautogui.click(x=agent.game.screen_size[0] / 2, y=agent.game.screen_size[1] / 2)
            solution = pacman_agent.astar_search()
            for move in solution:
                pyautogui.press(move)
                if pacman_agent.game.exit is True:
                    exit(2)
                if not pacman_agent.game.is_agent_active:
                    break
            pacman_agent.game.is_agent_active = False
        time.sleep(0.25)


if __name__ == '__main__':
    """
    Initialize pacman game and agent and create secondary thread for agent, since the main one will be used by tkinter 
    in order to display the GUI.
    """
    pacman = Pacman(WINDOW_HEIGHT, WINDOW_WIDTH)
    agent = Agent(pacman)
    agent_thread = threading.Thread(target=run_pacman_solution, args=[agent])
    agent_thread.start()
    pacman.launch_game()
