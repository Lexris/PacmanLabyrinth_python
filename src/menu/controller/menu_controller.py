from src.menu.view.menu_view import MenuView


class MenuController:
    def __init__(self, window_height, window_width):
        self.__menu = MenuView(window_height, window_width)

    def launch_menu(self):
        """
        The current thread will loop for tkinter in order to display the GUI.
        :return: difficulty chosen by the player
        """
        self.__menu.launch_menu()
        return self.__menu.last_selected_radio_button_rang
