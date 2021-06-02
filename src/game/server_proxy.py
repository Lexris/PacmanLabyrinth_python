import socket, pickle


class ServerProxy:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self._socket.connect((self.host, self.port))

    def get_solution_from_server(self, pacman_food_board_coords, pacman_board_coords, cost, heuristic, board):
        self._socket.sendall(pickle.dumps((pacman_food_board_coords, pacman_board_coords, cost, heuristic, board)))

        data = self._socket.recv(4096)
        if data:
            solution = pickle.loads(data)
        else:
            solution = []

        return solution

    def disconnect(self):
        self._socket.close()
