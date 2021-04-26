from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
import clinic




class Menu(Screen):

    def AddP(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'addp'

    def ShowAll(self):
         clinic.Clinic.show_all()
    def ShowP(self):
         clinic.Clinic.find_patient(0)
    def AddNote(self):
         #clinic.Clinic.find_patient(1)
         self.manager.transition = SlideTransition(direction="left")
         self.manager.current = 'addnote'



    def Relocate(self):
         clinic.Clinic.find_patient(2)
    def Monitor(self):
         clinic.Clinic.show_conditions()


    def ExitApp(self):
        App.get_running_app().stop()
