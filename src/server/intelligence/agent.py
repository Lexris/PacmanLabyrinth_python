from enum import Enum
from heapq import heappush, heappop
import socket, pickle
import ctypes


class Agent:
    __instance = None
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    @staticmethod
    def getInstance(pacman_food_board_coords, pacman_board_coords, cost, heuristic, board):
        if Agent.__instance is None:
            Agent(pacman_food_board_coords, pacman_board_coords, cost, heuristic, board)
        else:
            Agent.__instance.pacman_food_board_coords = pacman_food_board_coords
            Agent.__instance.pacman_board_coords = pacman_board_coords
            Agent.__instance.cost = cost
            Agent.__instance.heuristic = heuristic
            Agent.__instance.board = board
        return Agent.__instance

    def __init__(self, pacman_food_board_coords, pacman_board_coords, cost, heuristic, board):
        if Agent.__instance is None:
            self.pacman_food_board_coords = pacman_food_board_coords
            self.pacman_board_coords = pacman_board_coords
            self.cost = cost
            self.heuristic = heuristic
            self.board = board
            Agent.__instance = self

    def is_goal_state(self, state=None):
        """
        Check if pacman has reached the food.
        :param state: state to be checked; if None, current state of the game will be checked
        :return: True if state is goal state, False otherwise
        """
        if state:
            return state == self.pacman_food_board_coords
        else:
            return self.pacman_board_coords == self.pacman_food_board_coords

    def euclidean_heuristic(self, state_board_coords):
        """
        Compute euclidean distance heuristic for the astar algorithm. The distance is calculated in terms of the board
        positions(not the window positions). Window positions could also be used, but performance-wise it would be the
        same.
        :param state_board_coords: coordinates we'll calculate the heuristic for
        :return: heuristic distance value
        """
        xy1 = state_board_coords
        xy2 = self.pacman_food_board_coords
        return ((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2) ** 0.5

    def manhattan_heuristic(self, state_board_coords):
        """
        The Manhattan distance heuristic for a PositionSearchProblem
        :param state_board_coords: coordinates we'll calculate the heuristic for
        :return: heuristic distance value
        """
        xy1 = state_board_coords
        xy2 = self.pacman_food_board_coords
        return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

    DIAGONAL_HEURISTIC_MODE = Enum("CHEBYSHEV", "OCTILE")

    def diagonal_heuristic(self, state_board_coords, heuristic_mode):
        xy1 = state_board_coords
        xy2 = self.pacman_food_board_coords
        dx = abs(xy1[0] - xy2[0])
        dy = abs(xy1[1] - xy2[1])
        if heuristic_mode == "CHEBYSHEV":
            D = 1
            D2 = 1
        elif heuristic_mode == "OCTILE":
            D = 1
            D2 = 2 ** 0.5
        else:
            D = 1
            D2 = 1
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

    @staticmethod
    def get_successors(state, board):
        """
        Get all possible next moves for pacman
        :param state: state of the agent-controlled character within the game view
        :param board: the game view
        :return: list of possible moves
        """
        successors = []
        if state[1] + 1 < 18 and board[state[0]][state[1] + 1] == 0:
            successors.append(((state[0], state[1] + 1), 'd'))

        if state[0] + 1 < 18 and board[state[0] + 1][state[1]] == 0:
            successors.append(((state[0] + 1, state[1]), 's'))

        if state[1] - 1 >= 0 and board[state[0]][state[1] - 1] == 0:
            successors.append(((state[0], state[1] - 1), 'a'))

        if state[0] - 1 >= 0 and board[state[0] - 1][state[1]] == 0:
            successors.append(((state[0] - 1, state[1]), 'w'))
        return successors

    def get_selected_heuristic_value(self, state_board_coords):
        if self.heuristic == 0:
            return self.manhattan_heuristic(state_board_coords)
        elif self.heuristic == 1:
            return self.euclidean_heuristic(state_board_coords)
        elif self.heuristic == 2:
            return self.diagonal_heuristic(state_board_coords, "CHEBYSHEV")
        elif self.heuristic == 3:
            return self.diagonal_heuristic(state_board_coords, "OCTILE")
        else:
            return self.manhattan_heuristic

    # def get_selected_heuristic_value(self, state_board_coords):
    #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     s.connect((self.HOST, self.PORT))
    #     s.sendall(pickle.dumps((state_board_coords, self.pacman_food_board_coords, self.heuristic)))
    #     data = s.recv(4096)
    #     if data:
    #         data2 = pickle.loads(data)
    #         #print(data2)
    #         return data2
    #     s.close()
    #     return 0

    def astar_search(self):
        """
        Astar algorithm implementation.
        """
        current_state = self.pacman_board_coords
        action_list = []
        no_of_expanded_nodes = 0

        visited = []
        heap = []
        heappush(heap, (self.cost, current_state, action_list))

        while heap and not self.is_goal_state(current_state):
            no_of_expanded_nodes += 1
            heap_top = heappop(heap)
            current_state, action_list = (heap_top[i] for i in [1, 2])

            if current_state not in visited:
                visited.append(current_state)

            for successor in self.get_successors(current_state, self.board):
                if successor[0] not in visited:
                    heappush(heap, (
                        len(action_list) + 1 + self.get_selected_heuristic_value(successor[0]), successor[0],
                        action_list + [successor[1]]))

        print("Number of expanded nodes is " + str(no_of_expanded_nodes))

        return action_list
