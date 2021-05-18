import sqlite3
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition

from add_note import AddNote
from addp import AddP
from login_fail import login_fail
from menu import Menu


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
        if login=='' or password=='':
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'login_fail'
        elif self.check_credentials(login, password):
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'menu'
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
        manager.add_widget(Menu(name='menu'))
        manager.add_widget(AddP(name='addp'))
        manager.add_widget(AddNote(name='addnote'))
        manager.add_widget(login_fail(name='login_fail'))

        return manager