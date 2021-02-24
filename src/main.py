import threading
import time
import pyautogui

from src.game import Game
from src.utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH


def run_solution(solution):
    pyautogui.click(x=960, y=540)
    time.sleep(2)
    for move in solution:
        pyautogui.press(move)


if __name__ == '__main__':
    game = Game(WINDOW_HEIGHT, WINDOW_WIDTH)
    #agent_thread = threading.Thread(target=run_solution, args=[['s', 's', 'd', 'd', 'w', 'w']])
    #agent_thread.start()
    game.start_game()


