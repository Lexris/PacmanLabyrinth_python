import threading
import time
import pyautogui

from src.environment.pacman import Pacman
from src.intelligence.algorithms import astar_search
from src.utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH


def run_solution(game):
    pyautogui.click(x=960, y=540)
    time.sleep(2)
    solution = astar_search(game)
    for move in solution:
        pyautogui.press(move)


if __name__ == '__main__':
    pacman = Pacman(WINDOW_HEIGHT, WINDOW_WIDTH)
    agent_thread = threading.Thread(target=run_solution, args=[pacman])
    agent_thread.start()
    pacman.start_game()


