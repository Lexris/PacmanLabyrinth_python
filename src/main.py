import threading
import time

import pyautogui
from win32api import GetSystemMetrics

from src.game.controllers.game_controller import GameController
from src.menu.controller.menu_controller import MenuController
from src.utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH


def focus_new_window(screen_x, screen_y):
    time.sleep(0.20)
    pyautogui.click(x=screen_y / 2, y=screen_x / 2)


if __name__ == '__main__':
    screen_width, screen_height = GetSystemMetrics(0), GetSystemMetrics(1)

    pyautogui.FAILSAFE = False
    # create menu window
    menu_controller = MenuController(WINDOW_HEIGHT, WINDOW_WIDTH)
    # auto-focus next window
    agent_thread = threading.Thread(target=focus_new_window, args=(screen_height, screen_width))
    agent_thread.start()
    difficulty = menu_controller.launch_menu()

    # create game window
    pacman_controller = GameController(WINDOW_HEIGHT, WINDOW_WIDTH, difficulty)
    # auto-focus next window
    agent_thread = threading.Thread(target=focus_new_window, args=(screen_height, screen_width))
    agent_thread.start()
    pacman_controller.launch_game()
