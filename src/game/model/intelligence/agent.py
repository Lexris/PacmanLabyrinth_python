from heapq import heappush, heappop


class Agent:

    def __init__(self, game):
        self.game = game

    def euclidean_heuristic(self, state_board_coords):
        """
        Compute euclidean distance heuristic for the astar algorithm. The distance is calculated in terms of the board
        positions(not the window positions). Window positions could also be used, but performance-wise it would be the
        same.
        :param state_board_coords: coordinates we'll calculate the heuristic for
        :return: heuristic distance value
        """
        xy1 = state_board_coords
        xy2 = self.game.pacman_food_board_coords
        return ((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2) ** 0.5

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

    def astar_search(self):
        """
        Astar algorithm implementation.
        """
        current_state = self.game.pacman_board_coords
        action_list = []

        visited = []
        heap = []
        heappush(heap, (self.game.cost, current_state, action_list))

        while heap and not self.game.is_goal_state(current_state):
            heap_top = heappop(heap)
            current_state, action_list = (heap_top[i] for i in [1, 2])

            if current_state not in visited:
                visited.append(current_state)

            for successor in self.get_successors(current_state, self.game.board):
                if successor[0] not in visited:
                    heappush(heap, (
                        len(action_list) + 1 + self.euclidean_heuristic(successor[0]), successor[0],
                        action_list + [successor[1]]))

        return action_list
