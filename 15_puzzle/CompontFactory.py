from Button import Btn
from Windom import WindowForm
from Frame import Frame
from Label import Label


class Factory:
    __instance = None

    def __init__(self):
        if Factory.__instance is not None:
            raise Exception("Factory is a Singleton!")
        Factory.__instance = self

    @staticmethod
    def get_instance():
        if Factory.__instance is None:
            Factory()
        return Factory.__instance

    def create_button(self):
        return Btn()

    def create_window_form(self):
        return WindowForm()

    def create_label(self):
        return Label()

    def create_frame(self):
        return Frame()
