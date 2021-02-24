from src.utils.constants import PACMAN_BOARD_OBSTACLES_800x800, PACMAN_FOOD_POSITION


def euclidean_heuristic(position, goal):
    xy1 = position
    xy2 = goal
    return ((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2) ** 0.5


def is_goal_state(pacman_state):
    """
    Check if pacman hypothetical state has reached the food
    :return: True if goal state has been reached, False otherwise
    """
    if pacman_state == PACMAN_FOOD_POSITION:
        return True
    else:
        return False


def get_successors(pacman_state):
    """
    Get all possible next moves for pacman
    :return: list of possible moves
    """
    successors = []
    # pacman_board_coords = self.game.get_pacman_board_coords()
    if pacman_state[1] + 1 < 18 and PACMAN_BOARD_OBSTACLES_800x800[pacman_state[0]][
        pacman_state[1] + 1] == 0:
        successors.append(((pacman_state[0], pacman_state[1] + 1), 'd'))

    if pacman_state[0] + 1 < 18 and PACMAN_BOARD_OBSTACLES_800x800[pacman_state[0] + 1][
        pacman_state[1]] == 0:
        successors.append(((pacman_state[0] + 1, pacman_state[1]), 's'))

    if pacman_state[1] - 1 >= 0 and PACMAN_BOARD_OBSTACLES_800x800[pacman_state[0]][
        pacman_state[1] - 1] == 0:
        successors.append(((pacman_state[0], pacman_state[1] - 1), 'a'))

    if pacman_state[0] - 1 >= 0 and PACMAN_BOARD_OBSTACLES_800x800[pacman_state[0] - 1][
        pacman_state[1]] == 0:
        successors.append(((pacman_state[0] - 1, pacman_state[1]), 'w'))
    return successors


def astar_search(game, heuristic=euclidean_heuristic):
    """
    Expand cheapest node with respect to cost and heuristic.
    """

    from heapq import heappush, heappop

    current_state = game.get_pacman_board_coords()
    action_list = []

    visited = []
    heap = []
    heappush(heap, (0, current_state, action_list))

    while heap and not is_goal_state(current_state):
        heap_top = heappop(heap)
        current_state, action_list = (heap_top[i] for i in [1, 2])

        if current_state not in visited:
            visited.append(current_state)

        for successor in get_successors(current_state):
            if successor[0] not in visited:
                heappush(heap, (
                    len(action_list) + 1 + heuristic(successor[0], PACMAN_FOOD_POSITION), successor[0],
                    action_list + [successor[1]]))

    return action_list
