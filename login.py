import sqlite3
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from login_succ import login_succ
from login_fail import login_fail


class Login(Screen):
    def check_credentials(self, login, password):
        conn = sqlite3.connect('credentials.db')
        c = conn.cursor()
        r = c.execute("SELECT password FROM Credentials WHERE login=(?)", (login,))
        password_from_db = ''
        for row in r:
            password_from_db = row[0]

        if password == password_from_db:
            return True
        else:
            return False

    def do_login(self, login, password):
        app = App.get_running_app()
        app.login = login
        app.password = password

        if self.check_credentials(login, password):
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'login_succ'
        else:
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'login_fail'

    def reset_form(self):
        self.ids['login'].text = ''
        self.ids['password'].text = ''


class LoginApp(App):
    login = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))
        manager.add_widget(login_succ(name='login_succ'))
        manager.add_widget(login_fail(name='login_fail'))

        return manager
