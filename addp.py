from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
import clinic

class AddP(Screen):
    def Add(self):
        app = App.get_running_app()
        n = app.name
        ln = app.last_name
        mint = app.tempmin
        maxt = app.tempmax
        minh = app.hummin
        maxh = app.hummax
        light = app.light
        note = app.note


    def Back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'menu'

