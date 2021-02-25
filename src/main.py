import threading
import pyautogui

from src.environment.pacman import Pacman
from src.intelligence.agent import Agent
from src.utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH


def run_pacman_solution(pacman_agent):
    while True:
        if pacman_agent.game.is_agent_active:
            pyautogui.click(x=960, y=540)
            solution = pacman_agent.astar_search()
            for move in solution:
                pyautogui.press(move)
            break


if __name__ == '__main__':
    pacman = Pacman(WINDOW_HEIGHT, WINDOW_WIDTH)
    agent = Agent(pacman)
    agent_thread = threading.Thread(target=run_pacman_solution, args=[agent])
    agent_thread.start()
    pacman.start_game()
