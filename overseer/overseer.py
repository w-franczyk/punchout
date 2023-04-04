#!/usr/bin/python

from ScreenCategories import ScreenCategories
from ScreenDialogInfo import ScreenDialogInfo
from ScreenNewCategory import ScreenNewCategory

from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.properties import ListProperty
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.widget import Widget
from kivy.clock import Clock, mainthread
from threading import Thread
from typing import List
from rest import Rest, Board

class ScreenMain(Screen):
    boards: List[Board]

    def init(self):
        panel = TabbedPanel()

        for board in self.boards:
            if board.type == 'b':
                continue

            tab = TabbedPanelItem()
            tab.text = board.name
            tasks = TasksPanel()
            tasks.boardId = board.id
            tab.add_widget(tasks)
            self.manager.add_widget(tasks)
            panel.add_widget(tab)

        panel.default_tab = panel.tab_list[-2]
        self.add_widget(panel)


class ScreenLoading(Screen):
    pass

class Overseer(ScreenManager):
    screenCategories = None
    screenMain = None
    screenLoading = None
    screenNewCategory: ScreenNewCategory = None
    screenDialogInfo: ScreenDialogInfo = None

    def __init__(self, *args, **kwargs):
        super(Overseer, self).__init__(*args, **kwargs)
        self.screenLoading = ScreenLoading(name='screenLoading')
        self.add_widget(self.screenLoading)
        self.switch_to(self.screenLoading)
        self.screenMain = ScreenMain(name='screenMain')
        self.add_widget(self.screenMain)
        self.screenCategories = ScreenCategories(name='screenCategories')
        self.add_widget(self.screenCategories)
        self.screenNewCategory = ScreenNewCategory(name='screenNewCategory')
        self.add_widget(self.screenNewCategory)
        self.screenDialogInfo = ScreenDialogInfo(name='screenDialogInfo')
        self.add_widget(self.screenDialogInfo)

        Thread(target=self.getInitData).start()

    def getInitData(self):
        self.screenMain.boards = Rest.getBoards()
        self.finishInitialization()

    @mainthread
    def finishInitialization(self):
        self.screenMain.init()
        self.switch_to(self.screenMain)
        #self.switch_to(self.screenCategories)

class OverseerApp(App):
    app = None
    def build(self):
        self.app = Overseer()
        return self.app

class TasksPanel(Screen):
    boardId: int

    def btnCategoriesAction(self):
        screenCategories = self.manager.screenCategories
        screenCategories.boardId = self.boardId
        screenCategories.backActionScreen = self.manager.screenMain
        self.manager.switch_to(screenCategories)

class ColorLabel(Label):
    bgColor = ListProperty([0.0, 0.0, 0.0, 1])

class TasksRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(TasksRecycleView, self).__init__(**kwargs)
        self.data = [{'dataId': str(x), 'dataTitle': 'title {}'.format(x)} for x in range(100)]
        #self.data = [{'text': str(x)} for x in range(100)]

class TasksRecycleViewLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    pass

class TasksRecycleViewRow(RecycleDataViewBehavior, BoxLayout):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    bgColor = ListProperty([0.09, 0.09, 0.09, 1])
    borderColor = ListProperty([0.11, 0.11, 0.11, 1])

    # data fields
    dataId = StringProperty()
    dataTitle = StringProperty()

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(TasksRecycleViewRow, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(TasksRecycleViewRow, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        #rv.data.insert(0, 'dupa')
        #if is_selected:
        #    print("selection changed to {0}".format(rv.data[index]))
        #else:
        #    print("selection removed for {0}".format(rv.data[index]))

if __name__ == '__main__':
    OverseerApp().run()
