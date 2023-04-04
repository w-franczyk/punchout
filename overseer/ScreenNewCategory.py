from Common import PunchoutScreen
from rest import Rest

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('ScreenNewCategory.kv')

class ScreenNewCategory(PunchoutScreen):
    boardId: int = -1
    
    def btnNewCategoryAction(self):
        print('dupa')

    def btnOkWorker(self):
        if self.boardId < 0:
            raise Exception('Internal: boardId: {}'.format(self.boardId))

        if not self.ids.txtName.text:
            raise Exception('Name cannot be empty')

        Rest.addCategory(
                self.ids.txtName.text,
                self.ids.cpColor.hex_color,
                self.boardId)
    
    def btnOkSuccess(self):
        self.resetData()

    def resetData(self):
        boardId = -1
        self.ids.txtName.text = ''
        self.ids.cpColor.hex_color = '#ffffff'

    def on_leave(self):
        self.resetData()
