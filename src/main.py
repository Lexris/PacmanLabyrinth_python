import threading
import time

import pyautogui

from src.controllers.game_controller import GameController
from src.controllers.menu_controller import MenuController
from src.model.utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH


def focus_new_window():
    time.sleep(0.20)
    pyautogui.click(x=1920 / 2, y=1080 / 2)


if __name__ == '__main__':
    # create menu window
    menu_controller = MenuController(WINDOW_HEIGHT, WINDOW_WIDTH)
    agent_thread = threading.Thread(target=focus_new_window)
    agent_thread.start()
    difficulty = menu_controller.launch_menu()
    print(difficulty)
    # create game window
    pacman_controller = GameController(WINDOW_HEIGHT, WINDOW_WIDTH)
    # auto-focus next window
    agent_thread = threading.Thread(target=focus_new_window)
    agent_thread.start()
    pacman_controller.launch_game()
