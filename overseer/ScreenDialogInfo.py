from Common import PunchoutScreen

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('ScreenDialogInfo.kv')

class ScreenDialogInfo(PunchoutScreen):
    def setText(self, string):
        self.ids.lblTxt.text = string
