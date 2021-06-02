############################################## graphic/image paths ##################################################
PACMAN_IMAGE_PATH = 'resources/graphics/pacman_graphic.png'
PACMAN_FOOD_IMAGE_PATH = 'resources/graphics/pacman_food_graphic.png'

################################################# pacman board ######################################################
# formatting
PACMAN_BOARD_WINDOW_MARGIN = 6
PACMAN_BOARD_SIDE_SQUARES_NUMBER = 18
PACMAN_BOARD_SQUARE_SIDE_LENGTH = 44

# labyrinths
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
PACMAN_BOARD_OBSTACLES_MEDIUM = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
PACMAN_BOARD_OBSTACLES_EASY = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
PACMAN_BOARD_OBSTACLES = [PACMAN_BOARD_OBSTACLES_EASY, PACMAN_BOARD_OBSTACLES_MEDIUM, PACMAN_BOARD_OBSTACLES_DIFFICULT]

####################################################### pacman ######################################################
# formatting
PACMAN_MARGIN = 28

# pacman initial position on the window(px)
PACMAN_INITIAL_WINDOW_COORDS_EASY = (
    PACMAN_MARGIN + PACMAN_BOARD_SQUARE_SIDE_LENGTH * 4,
    PACMAN_MARGIN + PACMAN_BOARD_SQUARE_SIDE_LENGTH * 4
)
PACMAN_INITIAL_WINDOW_COORDS_MEDIUM = (
    PACMAN_MARGIN + PACMAN_BOARD_SQUARE_SIDE_LENGTH * 2,
    PACMAN_MARGIN + PACMAN_BOARD_SQUARE_SIDE_LENGTH * 2
)
PACMAN_INITIAL_WINDOW_COORDS_DIFFICULT = (PACMAN_MARGIN, PACMAN_MARGIN)

PACMAN_INITIAL_WINDOW_COORDS = [
    PACMAN_INITIAL_WINDOW_COORDS_EASY,
    PACMAN_INITIAL_WINDOW_COORDS_MEDIUM,
    PACMAN_INITIAL_WINDOW_COORDS_DIFFICULT
]

# pacman initial position on the board
PACMAN_INITIAL_BOARD_COORDS_DIFFICULT = (0, 0)
PACMAN_INITIAL_BOARD_COORDS_MEDIUM = (2, 2)
PACMAN_INITIAL_BOARD_COORDS_EASY = (4, 4)
PACMAN_INITIAL_BOARD_COORDS = [
    PACMAN_INITIAL_BOARD_COORDS_EASY,
    PACMAN_INITIAL_BOARD_COORDS_MEDIUM,
    PACMAN_INITIAL_BOARD_COORDS_DIFFICULT
]

# keys used for controlling pacman
PACMAN_CONTROLS = {
    'a',
    'w',
    'd',
    's'
}

# gives the angle pacman needs to be rotated by in order to face the direction represented by the pressed key
PACMAN_ORIENTATIONS = {

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

# displacement needed to pass from square to square, using the window coords(pixels) for movement
PACMAN_MOVEMENTS = {
    'a': (-PACMAN_BOARD_SQUARE_SIDE_LENGTH, 0),
    'w': (0, -PACMAN_BOARD_SQUARE_SIDE_LENGTH),
    'd': (PACMAN_BOARD_SQUARE_SIDE_LENGTH, 0),
    's': (0, PACMAN_BOARD_SQUARE_SIDE_LENGTH)
}

#################################################### food ###########################################################
# formatting
FOOD_MARGIN = 28

# food position on board
PACMAN_FOOD_BOARD_COORDS_EASY = (4, 13)
PACMAN_FOOD_BOARD_COORDS_MEDIUM = (2, 15)
PACMAN_FOOD_BOARD_COORDS_DIFFICULT = (2, 16)
PACMAN_FOOD_BOARD_COORDS = [
    PACMAN_FOOD_BOARD_COORDS_EASY,
    PACMAN_FOOD_BOARD_COORDS_MEDIUM,
    PACMAN_FOOD_BOARD_COORDS_DIFFICULT
]

# food position on window
PACMAN_FOOD_WINDOW_COORDS_EASY = (600, 204)
PACMAN_FOOD_WINDOW_COORDS_MEDIUM = (688, 116)
PACMAN_FOOD_WINDOW_COORDS_DIFFICULT = (732, 116)
PACMAN_FOOD_WINDOW_COORDS = [
    PACMAN_FOOD_WINDOW_COORDS_EASY,
    PACMAN_FOOD_WINDOW_COORDS_MEDIUM,
    PACMAN_FOOD_WINDOW_COORDS_DIFFICULT
]

################################################### utils ###########################################################
# tags
GRID_TAG = 'grid'
OBSTACLES_TAG = 'obstacles'
PACMAN_TAG = 'pacman'
PACMAN_FOOD_TAG = 'pacman_food'

# colors
BOARD_BACKGROUND_COLOR = '#262624'
BOARD_GRID_COLOR = '#ffff00'
BOARD_OBSTACLES_COLOR = '#ffff00'

# optimal solutions
EASY_SOLUTION_OPTIMAL_COST = 33
MEDIUM_SOLUTION_OPTIMAL_COST = 63
DIFFICULT_SOLUTION_OPTIMAL_COST = 68
SOLUTION_OPTIMAL_COST = [
    EASY_SOLUTION_OPTIMAL_COST,
    MEDIUM_SOLUTION_OPTIMAL_COST,
    DIFFICULT_SOLUTION_OPTIMAL_COST
]

# others
SCORE_NORMALIZATION_FACTOR = 10000
PACMAN_IMAGE_RESIZE_FACTOR = 40
PACMAN_FOOD_IMAGE_RESIZE_FACTOR = 40
CANVAS_CONFIG_BUX_FIX_MARGIN = 4

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server