#!/usr/bin/python

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class Overseer(Widget):
    pass

class OverseerApp(App):
    def build(self):
        return Overseer()

class BtnExport(Button):
    def on_release(self):
        print("export")

class BtnPrint(Button):
    def on_release(self):
        print("print selected")

class BtnNewTask(Button):
    def on_release(self):
        print("new task")

class BtnNewCategory(Button):
    def on_release(self):
        print("new category")

if __name__ == '__main__':
    OverseerApp().run()
