import clinic
import colors
import db_controller
from login import LoginApp


def main():
    # create() do stworzenia bd z hasłami do testów

    dbc = db_controller.DBController()  # declaring DB Controller
    C = clinic.Clinic()  # declaring clinic
    C.add_room()  # add room 0 - 2
    C.add_room()
    C.add_room()
    LoginApp().run()
    """
    for i in range(1, 4):
        room = db_controller.Room(number=i, size=3)
        dbc.add(room)
    """
    while 1:  # menu
        colors.pr_blue(
            "1 - Add patient\n2 - Show all\n3 - Show patient\n4 - Add note to patient\n5 - Relocate patient\n"
            "6 - Conditions monitor\n7 - Clear patients\n0 - Exit")
        x = int(input())
        if x == 1:
            C.add_patient()
        elif x == 2:
            C.show_all()
        elif x == 3:
            C.find_patient(0)
        elif x == 4:
            C.find_patient(1)
        elif x == 5:
            C.find_patient(2)
        elif x == 6:
            C.show_conditions()
        elif x == 7:
            dbc.clear_patients()
        elif x == 8:
            C.test()
        elif x == 0:
            exit()
        else:
            colors.pr_red("Wrong input data!")


if __name__ == '__main__':
    main()
