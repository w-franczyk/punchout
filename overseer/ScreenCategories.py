from Common import PunchoutScreen

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('ScreenCategories.kv')

class ScreenCategories(PunchoutScreen):
    boardId: int = -1

    #def on_pre_enter(self, *args):
    #    self.ids.test.text = str(self.boardId)
    def on_leave(self):
        print('leaving')

    def btnNewCategoryAction(self):
        screenNewCategory = self.manager.screenNewCategory
        screenNewCategory.boardId = self.boardId
        screenNewCategory.backActionScreen = self.manager.screenCategories
        self.manager.switch_to(screenNewCategory)

