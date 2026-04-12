from Button import Btn
from Windom import WindowForm
class Factory:
    __instance = None 
    def __init__(self):
        if Factory.__instance is not None:
            raise Exception("Factory is a Singleton! Use get_instance()")
        else:
            Factory.__instance = self
    @staticmethod
    def get_instance():
        if Factory.__instance is None:
            Factory()
        return Factory.__instance
    def create_button(self, parent, text, command):
        return Btn()
    def create_window_form(self):
        return WindowForm()
