import threading
import pyautogui
import socket, pickle

from src.game.view.pacman_view import PacmanView
import time


class GamePresenter:
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    def __init__(self, window_height, window_width, difficulty, heuristic):
        self._game = PacmanView(window_height, window_width, difficulty)
        self._heuristic = heuristic

        # bind specific pacman functionalities to canvas
        self._game.canvas.bind('<Configure>', self._game.setup_board)
        self._game.canvas.bind('<Key>', self._game.refresh_pacman)
        self._game.canvas.bind('<q>', self._game.toggle_agent)

    def __run_pacman_solution(self):
        """
        Secondary thread for the agent, activates when getting a 'q' event in the game and exists the program when getting
        an 'Escape' event.
        Time polling is used in other to reduce the resources used by the active waiting, since we need the agent to start
        only when/if it is initiated through the game event and the same goes for exiting the program.
        """
        while True:
            if self._game.game_state or self._game.exit:
                exit(2)
            elif self._game.agent_state:
                pyautogui.click(x=self._game.screen_size[0] / 2, y=self._game.screen_size[1] / 2)

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.HOST, self.PORT))
                s.sendall(pickle.dumps((self._game.pacman_food_board_coords, self._game.pacman_board_coords, self._game.cost, self._heuristic, self._game.board)))
                data = s.recv(4096)
                if data:
                    data2 = pickle.loads(data)
                    solution = data2
                    for move in solution:
                        pyautogui.press(move)
                        if self._game.exit is True:
                            exit(2)
                        if not self._game.agent_state:
                            break
                    self._game.agent_state = False
                    # print(data2)
                s.close()

            time.sleep(0.25)

    def should_exit(self):
        return self._game.exit

    def launch_game(self):
        """
        Create secondary thread for agent, since the main one will be used by tkinter in order to display the GUI.
        """
        agent_thread = threading.Thread(target=self.__run_pacman_solution)
        agent_thread.start()
        self._game.launch_game()
