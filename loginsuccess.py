from kivy.app import App
from kivy.uix.screenmanager import Screen


class LoginSuccess(Screen):
    def disconnect(self):
        # self.manager.transition = SlideTransition(direction="right")
        # self.manager.current = 'login'
        # self.manager.get_screen('login').resetForm()
        App.get_running_app().stop()
