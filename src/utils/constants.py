# window config
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
WINDOW_TITLE = 'Pacman Labyrinth'
WINDOW_LOGO_IMAGE_PATH = 'graphics/pacman_graphic_transparent.png'

# graphic paths
PACMAN_IMAGE_PATH = 'graphics/pacman_graphic.png'
PACMAN_FOOD_IMAGE_PATH = 'graphics/pacman_food_graphic.png'

# board constants
PACMAN_CONTROLS = {
    'a',
    'w',
    'd',
    's'
}
PACMAN_ORIENTATIONS = {
    # gives the angle the pacman image needs to be rotated by in order to face the direction of the pressed key
    'a': {
        0: 180,
        90: 90,
        180: 0,
        270: -90,
        360: -180
    },
    'w': {
        0: 90,
        90: 0,
        180: -90,
        270: -180,
        360: -270
    },
    'd': {
        0: 0,
        90: -90,
        180: -180,
        270: -270,
        360: -360
    },
    's': {
        0: 270,
        90: 180,
        180: 90,
        270: 0,
        360: -90
    }
}
PACMAN_MOVEMENTS = {
    'a': (-44, 0),
    'w': (0, -44),
    'd': (44, 0),
    's': (0, 44)
}
PACMAN_BOARD_OBSTACLES_800x800 = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
PACMAN_INITIAL_WINDOW_COORDS = (28, 28)
PACMAN_FOOD_BOARD_COORDS = (2, 16)
SOLUTION_OPTIMAL_COST = 68
# colors
BOARD_BACKGROUND_COLOR = '#262624'
GRID_LINES_COLOR = '#ffff00'
