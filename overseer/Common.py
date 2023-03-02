from kivy.uix.screenmanager import Screen

class PunchoutScreen(Screen):
    backActionScreen: Screen = None

    def btnBackAction(self):
        self.manager.switch_to(self.backActionScreen)
