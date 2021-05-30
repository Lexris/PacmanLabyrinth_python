from src.menu.utils.constants import *


class Observer:
    def __init__(self, view):
        self.view = view

    def actualizare_limba(self, rang_limba):
        self.view.difficulty_label['text'] = LABEL_TEXT[rang_limba]
        self.view.button['text'] = BUTTON_TEXT[rang_limba]
        self.view.radio_buttons[0]['text'] = RADIO_BUTTON0_TEXT[rang_limba]
        self.view.radio_buttons[1]['text'] = RADIO_BUTTON1_TEXT[rang_limba]
        self.view.radio_buttons[2]['text'] = RADIO_BUTTON2_TEXT[rang_limba]
        self.view.heuristic_radio_buttons[0]['text'] = HEURISTIC_BUTTON0_TEXT[rang_limba]
        self.view.heuristic_radio_buttons[1]['text'] = HEURISTIC_BUTTON1_TEXT[rang_limba]
        self.view.heuristic_radio_buttons[2]['text'] = HEURISTIC_BUTTON2_TEXT[rang_limba]
        self.view.heuristic_radio_buttons[3]['text'] = HEURISTIC_BUTTON3_TEXT[rang_limba]

