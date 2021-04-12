import tkinter

from PIL import Image, ImageTk

from src.utils.constants import *
from src.menu.model.utils.constants import *


class MenuView:
    def __init__(self, window_height, window_width):
        self.window = tkinter.Tk()
        self.window.title(WINDOW_TITLE)
        self.screen_size = (self.window.winfo_screenwidth(), self.window.winfo_screenheight())
        window_coord_x = self.screen_size[0] / 2 - window_width / 2
        window_coord_y = self.screen_size[1] / 2 - window_height / 2
        self.window.geometry('%dx%d+%d+%d' % (window_height, window_width + 50, window_coord_x, window_coord_y))
        self.window.iconphoto(False, tkinter.PhotoImage(file=WINDOW_LOGO_IMAGE_PATH))
        self.window.resizable(False, False)

        # init canvas and bind basic functionalities
        self.canvas = tkinter.Canvas(self.window, height=window_height, width=window_width, bg=MENU_BACKGROUND_COLOR)
        self.canvas.pack(fill=tkinter.BOTH, expand=True)

        # label for selecting difficulty
        self.difficulty_label = tkinter.Label(
            self.canvas,
            text=LABEL_TEXT,
            pady=20,
            width=window_width,
            background=MENU_ACCENT_COLOR,
            font=("Courier", 20)
        )
        self.difficulty_label.pack()

        # radio box for selecting difficulty
        self.difficultiesContainer = tkinter.StringVar(self.canvas)
        self.difficultiesContainer.set(0)
        difficulties = [
            (0, RADIO_BUTTON0_TEXT),
            (1, RADIO_BUTTON1_TEXT),
            (2, RADIO_BUTTON2_TEXT)
        ]
        self.radio_buttons = []
        for rang, difficulty in difficulties:
            r = tkinter.Radiobutton(
                self.canvas,
                variable=self.difficultiesContainer,
                text=difficulty,
                font=("Courier", 15),
                value=rang,
                indicator=0,
                background=MENU_BACKGROUND_COLOR,
                foreground=MENU_ACCENT_COLOR,
                activebackground=MENU_ACCENT_COLOR,
                activeforeground=MENU_BACKGROUND_COLOR,
                selectcolor=MENU_ACCENT_COLOR,
                highlightthickness=0
            )
            r.pack(fill=tkinter.X, ipady=5)
            self.radio_buttons.append(r)
        self.last_selected_radio_button_rang = 0

        # images representing difficulty
        self.difficulty_tkinter_images = []
        for image in PREVIEW_IMAGE_PATHS:
            difficulty_image = Image.open(image).resize(
                (PREVIEW_DIFFICULTY_IMAGE_RESIZE_FACTOR-100, PREVIEW_DIFFICULTY_IMAGE_RESIZE_FACTOR-100),
                Image.ANTIALIAS
            )
            self.difficulty_tkinter_images.append(ImageTk.PhotoImage(difficulty_image))
        self.difficulty_preview = tkinter.Label(self.canvas, bg=MENU_BACKGROUND_COLOR)
        self.difficulty_preview.pack()

        # radio box for selecting heuristic
        self.heuristicsContainer = tkinter.StringVar(self.canvas)
        self.heuristicsContainer.set(0)
        heuristics = [
            (0, HEURISTIC_BUTTON0_TEXT),
            (1, HEURISTIC_BUTTON1_TEXT),
            (2, HEURISTIC_BUTTON2_TEXT),
            (3, HEURISTIC_BUTTON3_TEXT)
        ]
        self.heuristic_radio_buttons = []
        for rang, heuristic in heuristics:
            r = tkinter.Radiobutton(
                self.canvas,
                variable=self.heuristicsContainer,
                text=heuristic,
                font=("Courier", 15),
                value=rang,
                indicator=0,
                background=MENU_BACKGROUND_COLOR,
                foreground=MENU_ACCENT_COLOR,
                activebackground=MENU_ACCENT_COLOR,
                activeforeground=MENU_BACKGROUND_COLOR,
                selectcolor=MENU_ACCENT_COLOR,
                highlightthickness=0
            )
            r.pack(fill=tkinter.X, ipady=5)
            self.heuristic_radio_buttons.append(r)
        self.last_selected_heuristic_radio_button_rang = 0

        # button for starting the game
        self.button = tkinter.Button(
            self.canvas,
            text=BUTTON_TEXT,
            font=("Courier", 40),
            width=window_width,
            background=MENU_ACCENT_COLOR,
            foreground=MENU_BACKGROUND_COLOR,
            activebackground=MENU_BACKGROUND_COLOR,
            activeforeground=MENU_ACCENT_COLOR,
        )
        self.button.pack()

        self.exit = False

    def launch_menu(self):
        """
        Launch the menu
        """
        self.window.mainloop()


