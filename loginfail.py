from kivy.uix.screenmanager import Screen, SlideTransition


class LoginFail(Screen):
    def to_login(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').reset_form()
