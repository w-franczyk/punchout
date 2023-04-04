from kivy.clock import Clock, mainthread
from kivy.uix.screenmanager import Screen
from typing import List
from threading import Thread
import time

class PunchoutScreen(Screen):
    backActionScreen: Screen = None

    def btnBackAction(self):
        self.manager.switch_to(self.backActionScreen)
    
    def btnOkAction(self):
        self.manager.switch_to(self.manager.screenLoading)
        Thread(target=self.btnOkWorkerWrapper).start()
    
    def btnOkWorkerWrapper(self):
        errorStr = ''
        try:
            self.btnOkWorker()
        except Exception as e:
            errorStr = str(e)

        Clock.schedule_once(lambda fn: self.btnOkWorkerFinished(errorStr))

    def btnOkWorkerFinished(self, errorStr):
        if errorStr:
            dialog = self.manager.screenDialogInfo
            dialog.setText('ERROR: ' + errorStr)
            dialog.backActionScreen = self
            self.manager.switch_to(dialog)
        else:
            self.btnBackAction()
            self.btnOkSuccess()

    def btnOkWorker(self):
        raise Exception("Not implemented")

    def btnOkSuccess(self):
        pass
