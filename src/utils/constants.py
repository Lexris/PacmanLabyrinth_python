# window config
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
WINDOW_TITLE = 'Pacman Labyrinth'
WINDOW_LOGO_IMAGE_PATH = 'graphics/pacman_graphic_transparent.png'

# graphic paths
PACMAN_IMAGE_PATH = 'graphics/pacman_graphic.png'
PACMAN_FOOD_IMAGE_PATH = 'graphics/pacman_food_graphic.png'

# pacman controls
PACMAN_CONTROLS = {
    # keys used for controlling pacman
    'a',
    'w',
    'd',
    's'
}
PACMAN_ORIENTATIONS = {
    # gives the angle pacman needs to be rotated by in order to face the direction represented by the pressed key
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
    # displacement needed to pass from square to square, using the window coords(pixels) for movement
    'a': (-44, 0),
    'w': (0, -44),
    'd': (44, 0),
    's': (0, 44)
}

# pacman board
PACMAN_BOARD_800x800_SIDE_SQUARES_NUMBER = 18
PACMAN_BOARD_800x800_SQUARE_SIDE_LENGTH = 44
PACMAN_BOARD_800x800_WINDOW_MARGIN = 6
PACMAN_BOARD_800x800_OBSTACLES = [
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
PACMAN_MARGIN = 28
FOOD_MARGIN = 28
PACMAN_INITIAL_WINDOW_COORDS = (28, 28)
PACMAN_FOOD_BOARD_COORDS = (2, 16)
SOLUTION_OPTIMAL_COST = 68

# tags
GRID_TAG = 'grid'
OBSTACLES_TAG = 'obstacles'
PACMAN_TAG = 'pacman'
PACMAN_FOOD_TAG = 'pacman_food'

# colors
BOARD_BACKGROUND_COLOR = '#262624'
GRID_COLOR = '#ffff00'
OBSTACLES_COLOR = '#ffff00'

# others
SCORE_NORMALIZATION_FACTOR = 10000
IMAGE_RESIZE_FACTOR = 40
