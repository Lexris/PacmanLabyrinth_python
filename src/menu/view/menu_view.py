import tkinter

from PIL import Image, ImageTk

from src.utils.constants import *
from src.menu.model.utils.constants import *


class MenuView:
    def __init__(self, window_height, window_width):
        self.__window = tkinter.Tk()
        self.__window.title(WINDOW_TITLE)
        self.screen_size = (self.__window.winfo_screenwidth(), self.__window.winfo_screenheight())
        window_coord_x = self.screen_size[0] / 2 - window_width / 2
        window_coord_y = self.screen_size[1] / 2 - window_height / 2
        self.__window.geometry('%dx%d+%d+%d' % (window_height, window_width, window_coord_x, window_coord_y))
        self.__window.iconphoto(False, tkinter.PhotoImage(file=WINDOW_LOGO_IMAGE_PATH))
        self.__window.resizable(False, False)
        self.__window.protocol('WM_DELETE_WINDOW', self._exit_protocol)

        # init canvas and bind basic functionalities
        self.__canvas = tkinter.Canvas(self.__window, height=window_height, width=window_width,
                                       bg=MENU_BACKGROUND_COLOR)
        self.__canvas.pack(fill=tkinter.BOTH, expand=True)
        self.__canvas.bind('<1>', lambda event: self.__canvas.focus_set())
        self.__canvas.bind('<Escape>', self._exit_protocol)

        # label for selecting difficulty
        self.difficulty_label = tkinter.Label(
            self.__canvas,
            text="Please select the desired difficulty",
            pady=20,
            width=window_width,
            background=MENU_ACCENT_COLOR,
            font=("Courier", 20)
        )
        self.difficulty_label.pack()

        # radio box for selecting difficulty
        self.__difficultiesContainer = tkinter.StringVar(self.__canvas)
        self.__difficultiesContainer.set(0)
        difficulties = [
            (0, "Just wanna relax :)"),
            (1, "I'll go for normal, thanks!"),
            (2, "  I'm so looking for a headache...")
        ]
        self.radio_buttons = []
        for rang, difficulty in difficulties:
            r = tkinter.Radiobutton(
                self.__canvas,
                variable=self.__difficultiesContainer,
                command=self.radio_buttons_bind,
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
                (PREVIEW_DIFFICULTY_IMAGE_RESIZE_FACTOR, PREVIEW_DIFFICULTY_IMAGE_RESIZE_FACTOR),
                Image.ANTIALIAS
            )
            self.difficulty_tkinter_images.append(ImageTk.PhotoImage(difficulty_image))
        self.difficulty_preview = tkinter.Label(self.__canvas, bg=MENU_BACKGROUND_COLOR)
        self.difficulty_preview.pack()

        # init radiobutton and difficulty preview image
        self.radio_buttons[1].invoke()

        # button for starting the game
        self.button = tkinter.Button(
            self.__canvas,
            text="Start game",
            font=("Courier", 40),
            width=window_width,
            background=MENU_ACCENT_COLOR,
            foreground=MENU_BACKGROUND_COLOR,
            activebackground=MENU_BACKGROUND_COLOR,
            activeforeground=MENU_ACCENT_COLOR,
            command=lambda: self.terminate_menu(self.last_selected_radio_button_rang)
        )
        self.button.pack()

    def radio_buttons_bind(self):
        selected_radio_button_rang = int(self.__difficultiesContainer.get())
        self.radio_buttons[self.last_selected_radio_button_rang].configure(foreground=MENU_ACCENT_COLOR,
                                                                           background=MENU_BACKGROUND_COLOR)
        self.radio_buttons[selected_radio_button_rang].configure(foreground=MENU_BACKGROUND_COLOR,
                                                                 background=MENU_ACCENT_COLOR)
        self.difficulty_preview.configure(image=self.difficulty_tkinter_images[selected_radio_button_rang])
        self.difficulty_preview.image = self.difficulty_tkinter_images[selected_radio_button_rang]
        self.last_selected_radio_button_rang = selected_radio_button_rang

    def _exit_protocol(self, event=None):
        """
        Exit the program
        :param event: will be an <Esc> event or None
        """
        self.__window.destroy()
        self.exit = True

    def launch_menu(self):
        """
        Launch the menu
        """
        self.__window.mainloop()

    def terminate_menu(self, rang):
        self.__window.destroy()
