from text import Label
from Button import Btn
from Windom import WindowForm
from Frame import Frame
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
    def create_button(self):
        return Btn()
    def create_window_form(self):
        return WindowForm()
    def createLabel(self, parent, text):
        return Label()
    def CreateFrame(self):
        return Frame()