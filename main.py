import clinic
import colors
import db_controller
from login import LoginApp


def main():
    # create() do stworzenia bd z hasłami do testów
    LoginApp().run()
    dbc = db_controller.DBController()  # declaring DB Controller
    C = clinic.Clinic()  # declaring clinic
    C.addRoom()  # add room 0 - 2
    C.addRoom()
    C.addRoom()
    for i in range(1, 4):
        room = db_controller.Room(number=i, size=5)
        dbc.add(room)

    while 1:  # menu
        colors.prLightPurple("1 - Add patient\n2 - Show all\n0 - Exit")
        x = int(input())
        if x == 1:
            C.addPatient()
        elif x == 2:
            C.showAll()
        elif x == 3:
            C.test()
        elif x == 0:
            exit()
        else:
            colors.prRed("Wrong input data!")


if __name__ == '__main__':
    main()
