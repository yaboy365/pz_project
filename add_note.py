from datetime import datetime

from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

import db_controller
from menu import Menu


class AddNote(Screen):
    custom_date = ObjectProperty(None)

    patient_id=StringProperty(None)

    # assesment_type = StringProperty(None)
    # assesment_result = StringProperty(None)
    # assesment_remarks=StringProperty(None)
    # date=StringProperty(None)

#     def Add(self):
#         app = App.get_running_app()
#
    def build(self):
        manager = ScreenManager()
        #manager.add_widget(AddNote(name='addnote'))
        # manager.add_widget(LoginSuccess(name='login_succ'))
        # manager.add_widget(LoginFail(name='login_fail'))
        manager.add_widget(Menu(name='menu'))
        # manager.add_widget(AddP(name='addp'))
        return manager
    def reset_form(self):
        self.ids['patient_id'].text = ''
        self.ids['assesment_type'].text = ''
        self.ids['assesment_result'].text = ''
        self.ids['assesment_remarks'].text = ''
        self.ids['custom_date'].text = 'Please enter date in DD/MM/YY HH:MM:SS format'
        self.ids['custom_date'].opacity=0
        #przydałoby się zresetować stan checkboxów



    def backToMenu(self):
        self.reset_form()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'menu'
    def submit(self,patient_id,assesment_type,assesment_result,assesment_remarks,date):
        if date=='Please enter date in DD/MM/YY HH:MM:SS format' or date=='':
            date=datetime.now()
            date = date.strftime("%d/%m/%Y %H:%M:%S")
        else:
            date = datetime.strptime(date, '%d/%m/%y %H:%M:%S')


        assesment_entrance = assesment_type + '|' + assesment_result + '|' +assesment_remarks + '|'+str(date)
        dbc = db_controller.DBController()
        #db_p=dbc.
        #dbc.add(db_p)


        print(assesment_entrance)
        self.reset_form()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'menu'




