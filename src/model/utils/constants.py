# window config
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
WINDOW_TITLE = 'Pacman Labyrinth'
WINDOW_LOGO_IMAGE_PATH = 'graphics/pacman_graphic_transparent.png'

# graphic/image paths
PACMAN_IMAGE_PATH = 'graphics/pacman_graphic.png'
PACMAN_FOOD_IMAGE_PATH = 'graphics/pacman_food_graphic.png'
DIFFICULT_PREVIEW_IMAGE_PATH = 'graphics/difficult_preview.png'

# pacman board
PACMAN_BOARD_WINDOW_MARGIN = 6
PACMAN_BOARD_SIDE_SQUARES_NUMBER = 18
PACMAN_BOARD_SQUARE_SIDE_LENGTH = 44
PACMAN_BOARD_OBSTACLES_DIFFICULT = [
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
PACMAN_BOARD_OBSTACLES_EASY = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
PACMAN_BOARD_OBSTACLES = [PACMAN_BOARD_OBSTACLES_EASY, PACMAN_BOARD_OBSTACLES_DIFFICULT]
# pacman
PACMAN_MARGIN = 28
PACMAN_INITIAL_WINDOW_COORDS_DIFFICULT = (PACMAN_MARGIN, PACMAN_MARGIN)
PACMAN_INITIAL_WINDOW_COORDS_EASY = (
    PACMAN_MARGIN + PACMAN_BOARD_SQUARE_SIDE_LENGTH * 4,
    PACMAN_MARGIN + PACMAN_BOARD_SQUARE_SIDE_LENGTH * 4
)
PACMAN_INITIAL_WINDOW_COORDS = [PACMAN_INITIAL_WINDOW_COORDS_EASY, PACMAN_INITIAL_WINDOW_COORDS_DIFFICULT]
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
    'a': (-PACMAN_BOARD_SQUARE_SIDE_LENGTH, 0),
    'w': (0, -PACMAN_BOARD_SQUARE_SIDE_LENGTH),
    'd': (PACMAN_BOARD_SQUARE_SIDE_LENGTH, 0),
    's': (0, PACMAN_BOARD_SQUARE_SIDE_LENGTH)
}

# food
FOOD_MARGIN = 28
PACMAN_FOOD_BOARD_COORDS_EASY = (4, 13)
PACMAN_FOOD_BOARD_COORDS_DIFFICULT = (2, 16)
PACMAN_FOOD_BOARD_COORDS = [PACMAN_FOOD_BOARD_COORDS_EASY, PACMAN_FOOD_BOARD_COORDS_DIFFICULT]

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
SOLUTION_OPTIMAL_COST = 68
CANVAS_CONFIG_BUX_FIX_MARGIN = 4
SCORE_NORMALIZATION_FACTOR = 10000
IMAGE_RESIZE_FACTOR = 40
