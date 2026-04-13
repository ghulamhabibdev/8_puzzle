from ast import List
import select
from Button import Btn
from Windom import WindowForm
from query import Query
from DB import DB
from CompontFactory import Factory
class FifteenPuzzle:
    WindowFormList = []
    WindowFormList

    def __init__(self):
        pass

    def addWindform(self, window_form):
        self.WindowFormList.append(window_form)

    def getForm(self, index):
        return self.WindowFormList[index]

    def Run(
        self,
    ):
        WindowFor = self.WindowFormList[0]
        WindowFor.run()

    def Stop(self):
        pass

    def deleteQuery(self, query):
        pass

    def SaveQuery(self, query):
        pass

    def UpdateQuery(self, query):
        pass

    def LoadQuery(self, query):
        pass

    def ExecuteQuery(self, query):
        pass

    def ShowPlayerName(self, player_name):
        pass

    def ShowPlayerScore(self, player_score):
        pass

    def ShowPlayerStats(self, player_stats):
        pass

    def Winer(self, player_name):
        pass

    def loadCongurationWindow(self):
        pass

    def loadHelpWindow(self):
        pass

    def loadMainMenu(self):
        pass

    def LoadBoard(self):
        pass

    def Exit(self):
        pass


print("Game is Start Stay Tuned!")
factory = Factory.get_instance()
HomeForm = factory.create_window_form()
frame=factory.create_frame();
btn = factory.create_button()
btn.SetParent(HomeForm.GetBody())
# btn.SetText("Start Game")
# btn.setColor("blue")
HomeForm.addCustomButton(btn)
frame.SetParent(HomeForm.GetBody())
frame.AddButton(btn)
frame.SetHeight(10)
frame.SetWidth(100)
frame.SetBackgroundColor("lightgray")
HomeForm.AddFrame(frame)
HomeForm.run()
