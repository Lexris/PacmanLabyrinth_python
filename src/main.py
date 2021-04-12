import threading
import time

import pyautogui
from win32api import GetSystemMetrics

from src.game.presenter.game_controller import GamePresenter
from src.menu.presenter.menu_controller import MenuPresenter
from src.utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH


def focus_new_window(screen_x, screen_y):
    time.sleep(0.20)
    pyautogui.click(x=screen_y / 2, y=screen_x / 2)


if __name__ == '__main__':
    screen_width, screen_height = GetSystemMetrics(0), GetSystemMetrics(1)
    pyautogui.FAILSAFE = False

    while True:
        # create menu window
        menu_controller = MenuPresenter(WINDOW_HEIGHT, WINDOW_WIDTH)
        # auto-focus next window
        agent_thread = threading.Thread(target=focus_new_window, args=(screen_height, screen_width))
        agent_thread.start()
        difficulty, heuristic = menu_controller.select_game_settings()
        if menu_controller.should_exit():
            break

        # create game window
        pacman_controller = GamePresenter(WINDOW_HEIGHT, WINDOW_WIDTH, difficulty, heuristic)
        # auto-focus next window
        agent_thread = threading.Thread(target=focus_new_window, args=(screen_height, screen_width))
        agent_thread.start()
        pacman_controller.launch_game()
        if pacman_controller.should_exit():
            break
