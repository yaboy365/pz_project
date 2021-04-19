import patient
import room
import colors
import db_controller


class Clinic:  # clinic class
    def __init__(self):
        self.__rooms = []  # rooms collection
        self.__nextRoomID = 0  # first free id for a room
        self.__nextPatientID = 0  # first free id for a patient

    def test(self):
        p = patient.Patient()
        p.ID = 50
        p.name = "Testo"
        p.lastName = "Viron"
        p.tempMin = 17
        p.tempMax = 25
        number = 0
        for r in self.__rooms:
            if r.get_ID() == number:
                r.add(p)

    @staticmethod
    def gather_data():
        p = patient.Patient()  # Patient var declaration, getting input from user
        colors.pr_blue("Enter patient name: ")
        p.name = str(input())
        colors.pr_blue("Enter patient last name: ")
        p.lastName = str(input())
        colors.pr_blue("Does patient have temperature determinant?")
        colors.pr_green("1 - Yes")  # custom temp compartment
        colors.pr_red("2 - No")
        x = int(input())
        if x == 1:  # getting min - max temp from user
            colors.pr_blue("Enter minimal temperature value: ")
            p.tempMin = float(input())
            colors.pr_blue("Enter maximal temperature value: ")
            p.tempMax = float(input())
        elif x == 2:  # setting default temp
            colors.pr_blue("Setting default values.")
        else:
            colors.pr_red("Wrong input data!")
        return p

    def add_patient(self):  # adds a patient to selected room if possible
        dbc = db_controller.DBController()  # DB Controller declaration
        while 1:
            p = self.gather_data()
            colors.pr_blue("Do you want to add this patient?")  # confirmation
            colors.pr_blue("Name: " + p.name + " " + p.lastName)
            colors.pr_blue("Temperature compartment: "
                           + str(p.tempMin) + "°C - " + str(p.tempMax) + "°C")
            colors.pr_green("1 - Yes")
            colors.pr_red("2 - No")
            colors.pr_yellow("3 - Enter data again")  # enter patient data again
            x = int(input())
            if x == 1:  # adding patient
                p.ID = int(self.__nextPatientID)  # generating id
                self.__nextPatientID += 1  # incrementing to next free value
                flag = 1
                while flag == 1:
                    for r in self.__rooms:
                        colors.pr_cyan("Room #" + str(r.get_ID()))
                        r.show_patients()
                    colors.pr_blue("Enter room number: ")
                    number = int(input())

                    for i in self.__rooms:
                        if i.get_ID() == number:
                            if i.add(p) == 1:
                                db_p = db_controller.Patient(name=p.name, surname=p.lastName, temp_max=p.tempMax,
                                                             temp_min=p.tempMin,
                                                             room=number + 1)  # Creation of Patient for DB
                                dbc.add(db_p)  # Adding Patient into DB
                                flag = 0
                                break
                            else:
                                colors.pr_green("1 - Another room")
                                colors.pr_red("2 - Abort")
                                flag = int(input())
                    if flag == 2:
                        self.__nextPatientID -= 1
                break
            elif x == 2:  # aborting
                colors.pr_red("Aborted.")
                break
            elif x == 3:  # new data
                continue
            else:
                colors.pr_red("Wrong input data!")

    def add_room(self):  # generates and adds to collection new room
        self.__rooms.append(room.Room(int(self.__nextRoomID)))
        self.__nextRoomID += 1

    def show_all(self):
        db_controller.print_rooms()
        db_controller.print_patient()
        for i in self.__rooms:
            colors.pr_cyan("Room #" + str(i.get_ID()))
            i.show_patients()
