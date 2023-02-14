#!/usr/bin/python

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

class ScreenMain(Screen):
    def init(self):
        panel = TabbedPanel()

        for tabName in ['tab1', 'tab2', 'tab3']:
            item = TabbedPanelItem()
            item.text = tabName
            tasks = TasksPanel()
            item.add_widget(tasks)
            self.manager.add_widget(tasks)
            panel.add_widget(item)

        panel.default_tab = panel.tab_list[-2]
        self.add_widget(panel)

class ScreenAddCategory(Screen):
    pass

class Overseer(ScreenManager):
    screenAddCategory = None
    screenMain = None

    def __init__(self, *args, **kwargs):
        super(Overseer, self).__init__(*args, **kwargs)
        self.screenMain = ScreenMain(name='screenMain')
        self.screenAddCategory = ScreenAddCategory(name='screenAddCategory')

        self.add_widget(self.screenMain)
        self.add_widget(self.screenAddCategory)

        self.screenMain.init()
        self.switch_to(self.screenMain)

class OverseerApp(App):
    def build(self):
        return Overseer()

class TasksPanel(Screen):
#    manager = None

#    def __init__(self, screenManager, *args, **kwargs):
#        super(TasksPanel, self).__init__(*args, **kwargs)
#        self.manager = screenManager
    pass

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
