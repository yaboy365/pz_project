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
            if r.getID() == number:
                r.add(p)

    def addPatient(self):  # adds a patient to selected room if possible
        dbc = db_controller.DBController()  # DB Controller declaration
        while 1:
            p = patient.Patient()  # Patient var declaration, getting input from user
            colors.prLightPurple("Enter patient name: ")
            p.name = str(input())
            colors.prLightPurple("Enter patient last name: ")
            p.lastName = str(input())
            colors.prLightPurple("Does patient have temperature determinant?")
            colors.prGreen("1 - Yes")  # custom temp compartment
            colors.prRed("2 - No")
            x = int(input())
            if x == 1:  # getting min - max temp from user
                colors.prLightPurple("Enter minimal temperature value: ")
                p.tempMin = float(input())
                colors.prLightPurple("Enter maximal temperature value: ")
                p.tempMax = float(input())
            elif x == 2:  # setting default temp
                colors.prLightPurple("Setting default values.")
            else:
                colors.prRed("Wrong input data!")

            colors.prLightPurple("Do you want to add this patient?")  # confirmation
            colors.prLightPurple("Name: " + p.name + " " + p.lastName)
            colors.prLightPurple("Temperature compartment: "
                                 + str(p.tempMin) + "°C - " + str(p.tempMax) + "°C")
            colors.prGreen("1 - Yes")
            colors.prRed("2 - No")
            colors.prYellow("3 - Enter data again")  # enter patient data again
            x = int(input())
            if x == 1:  # adding patient
                p.ID = int(self.__nextPatientID)  # generating id
                self.__nextPatientID += 1  # incrementing to next free value
                flag = 1
                while flag == 1:
                    for r in self.__rooms:
                        colors.prCyan("Room #" + str(r.getID()))
                        r.showPatients()
                    colors.prLightPurple("Enter room number: ")
                    number = int(input())

                    for i in self.__rooms:
                        if i.getID() == number:
                            if i.add(p) == 1:
                                db_p = db_controller.Patient(name=p.name, surname=p.lastName, temp_max=p.tempMax,
                                                             temp_min=p.tempMin,
                                                             room=number + 1)  # Creation of Patient for DB
                                dbc.add(db_p)  # Adding Patient into DB
                                flag = 0
                                break
                            else:
                                colors.prGreen("1 - Another room")
                                colors.prRed("2 - Abort")
                                flag = int(input())
                    if flag == 2:
                        self.__nextPatientID -= 1
                break
            elif x == 2:  # aborting
                colors.prRed("Aborted.")
                break
            elif x == 3:  # new data
                continue
            else:
                colors.prRed("Wrong input data!")

    def addRoom(self):  # generates and adds to collection new room
        self.__rooms.append(room.Room(int(self.__nextRoomID)))
        self.__nextRoomID += 1

    def showAll(self):
        db_controller.printRooms()
        db_controller.printPatient()
        for i in self.__rooms:
            colors.prCyan("Room #" + str(i.getID()))
            i.showPatients()
