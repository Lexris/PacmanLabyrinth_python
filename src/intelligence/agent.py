from src.utils.constants import PACMAN_BOARD_OBSTACLES_800x800


class Agent:
    def __init__(self, game):
        self.game = game

    def is_goal_state(self):
        pacman_compared_position = (
            int((self.game.pacman_position[0] - 28) / 44),
            int((self.game.pacman_position[1] - 28) / 44)
        )
        if pacman_compared_position == (self.game.window.winfo_width() - 1 * 44 - 28, 28 + 2 * 44):
            return True
        else:
            return False

    def get_successors(self):
        successors = []
        pacman_compared_position = (
            int((self.game.pacman_position[0] - 28) / 44),
            int((self.game.pacman_position[1] - 28) / 44)
        )
        if PACMAN_BOARD_OBSTACLES_800x800[pacman_compared_position[1] + 1][self.game.pacman_position[0]] == 0:
            successors.append('d')
        if PACMAN_BOARD_OBSTACLES_800x800[pacman_compared_position[1]][self.game.pacman_position[0] + 1] == 0:
            successors.append('w')
        if PACMAN_BOARD_OBSTACLES_800x800[pacman_compared_position[1] - 1][self.game.pacman_position[0]] == 0:
            successors.append('a')
        if PACMAN_BOARD_OBSTACLES_800x800[pacman_compared_position[1]][self.game.pacman_position[0] - 1] == 0:
            successors.append('s')
        print(successors)

