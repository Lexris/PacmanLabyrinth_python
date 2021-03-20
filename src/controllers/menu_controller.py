from src.starting_menu.menu import Menu


class MenuController:
    def __init__(self, window_height, window_width):
        self.__menu = Menu(window_height, window_width)

    def launch_menu(self):
        """
        The current thread will loop for tkinter in order to display the GUI.
        """
        self.__menu.launch_menu()
        return self.__menu.last_selected_radio_button_rang
