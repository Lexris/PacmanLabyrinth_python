from src.menu.model.observer import Observer
from src.menu.view.menu_view import MenuView
from src.menu.model.utils.constants import *


class MenuPresenter:
    def __init__(self, window_height, window_width):
        self.__menu = MenuView(window_height, window_width)
        self.observer = Observer(self.__menu)

        # attach custom exit protocol to 'x' exiting icon
        self.__menu.window.protocol('WM_DELETE_WINDOW', self._exit_protocol)

        # give canvas focus so bindings within canvas are not
        self.__menu.canvas.bind('<1>', lambda event: self.__menu.canvas.focus_set())

        # give user the option to quit game by pressing the Escape key
        self.__menu.window.bind('<Escape>', self._exit_protocol)

        # bind radio buttons to update group appearance
        for rb in self.__menu.radio_buttons:
            rb.config(command=self._radio_buttons_bind)

        for rb in self.__menu.heuristic_radio_buttons:
            rb.config(command=self._heuristic_radio_buttons_bind)

        for rb in self.__menu.languages_radio_buttons:
            rb.config(command=self._language_radio_buttons_bind)

        # init radiobutton and difficulty preview image
        self.__menu.radio_buttons[1].invoke()
        self.__menu.heuristic_radio_buttons[0].invoke()
        self.__menu.languages_radio_buttons[0].invoke()

        # bind submit button to start game with selected difficulty
        self.__menu.button.config(command=lambda: self.terminate_menu())

    def _radio_buttons_bind(self):
        """
        Update appearance of the lastly and newly pressed radio buttons
        """
        selected_radio_button_rang = int(self.__menu.difficultiesContainer.get())
        self.__menu.radio_buttons[self.__menu.last_selected_radio_button_rang].configure(foreground=MENU_ACCENT_COLOR,
                                                                                         background=MENU_BACKGROUND_COLOR)
        self.__menu.radio_buttons[selected_radio_button_rang].configure(foreground=MENU_BACKGROUND_COLOR,
                                                                        background=MENU_ACCENT_COLOR)
        self.__menu.difficulty_preview.configure(
            image=self.__menu.difficulty_tkinter_images[selected_radio_button_rang])
        self.__menu.difficulty_preview.image = self.__menu.difficulty_tkinter_images[selected_radio_button_rang]
        self.__menu.last_selected_radio_button_rang = selected_radio_button_rang

    def _heuristic_radio_buttons_bind(self):
        """
        Update appearance of the lastly and newly pressed radio buttons
        """
        selected_heuristic_radio_button_rang = int(self.__menu.heuristicsContainer.get())
        self.__menu.heuristic_radio_buttons[self.__menu.last_selected_heuristic_radio_button_rang].configure(foreground=MENU_ACCENT_COLOR,
                                                                                         background=MENU_BACKGROUND_COLOR)
        self.__menu.heuristic_radio_buttons[selected_heuristic_radio_button_rang].configure(foreground=MENU_BACKGROUND_COLOR,
                                                                        background=MENU_ACCENT_COLOR)
        self.__menu.last_selected_heuristic_radio_button_rang = selected_heuristic_radio_button_rang

    def _language_radio_buttons_bind(self):
        """
        Update appearance of the lastly and newly pressed radio buttons
        """
        selected_language_radio_button_rang = int(self.__menu.languagesContainer.get())
        self.__menu.languages_radio_buttons[self.__menu.last_selected_language_radio_button_rang].configure(foreground=MENU_ACCENT_COLOR,
                                                                                         background=MENU_BACKGROUND_COLOR)
        self.__menu.languages_radio_buttons[selected_language_radio_button_rang].configure(foreground=MENU_BACKGROUND_COLOR,
                                                                        background=MENU_ACCENT_COLOR)
        self.__menu.last_selected_language_radio_button_rang = selected_language_radio_button_rang
        self.observer.actualizare_limba(selected_language_radio_button_rang)

    def _exit_protocol(self, event=None):
        """
        Exit the program
        :param event: will be an <Esc> event or None
        """
        self.__menu.window.destroy()
        self.__menu.exit = True

    def should_exit(self):
        return self.__menu.exit

    def terminate_menu(self):
        self.__menu.window.destroy()

    def select_game_settings(self):
        """
        The current thread will loop for tkinter in order to display the GUI.
        :return: difficulty chosen by the player
        """
        self.__menu.launch_menu()
        return self.__menu.last_selected_radio_button_rang, self.__menu.last_selected_heuristic_radio_button_rang
