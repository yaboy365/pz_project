import sqlite3
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition

from add_note import AddNote
from clinic import Clinic
from loginsuccess import LoginSuccess
from loginfail import LoginFail
from menu import Menu
from addp import AddP

class Login(Screen):
    @staticmethod
    def check_credentials(login, password):
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
            #self.manager.current = 'login_succ'
            self.manager.current = 'menu'
            #self.manager.current = 'add_note'
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
        manager.add_widget(LoginSuccess(name='login_succ'))
        manager.add_widget(LoginFail(name='login_fail'))
        manager.add_widget(Menu(name='menu'))
        manager.add_widget(AddNote(name='addnote'))
        manager.add_widget(AddP(name='addp'))
        #manager.add_widget(AddNote(name='add_note'))

        return manager
