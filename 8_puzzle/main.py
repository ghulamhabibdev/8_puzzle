from ast import List
import tkinter as tk
from Button import Btn
from Windom import WindowForm
from query import Query
from db import DB
from  CompontFactory import Factory
window = WindowForm()
window.run()
class EightPuzzle:
    WindowFormList=List()
    WindowFormList
    def __init__(self):
        pass
    def addWindform(self, window_form, formNumber):
        self.WindowFormList.append([window_form,formNumber])
    def getForm(self, index):
        return self.WindowFormList[index]
    def Run(self):
        pass
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
    