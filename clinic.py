from datetime import datetime

import patient
import room
import colors
import db_controller


class Clinic:  # clinic class
    def __init__(self):
        self.__rooms = []  # rooms collection
        self.__nextRoomID = 1  # first free id for a room
        self.__nextPatientID = 1  # first free id for a patient

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
    def gather_data():  # gathering input from user
        p = patient.Patient()  # Patient var declaration, getting input from user
        colors.pr_blue("Enter patient name: ")
        p.name = str(input())
        colors.pr_blue("Enter patient last name: ")
        p.lastName = str(input())
        # temp
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
        # humidity
        colors.pr_blue("Does patient have humidity determinant?")
        colors.pr_green("1 - Yes")  # custom humidity compartment
        colors.pr_red("2 - No")
        x = int(input())
        if x == 1:  # getting min - max humidity from user
            colors.pr_blue("Enter minimal humidity value: ")
            p.humMin = float(input())
            colors.pr_blue("Enter maximal humidity value: ")
            p.humMax = float(input())
        elif x == 2:  # setting default humidity
            colors.pr_blue("Setting default values.")
        else:
            colors.pr_red("Wrong input data!")
        # light
        colors.pr_blue("Does patient have light determinant?")
        colors.pr_green("1 - Yes")
        colors.pr_red("2 - No")
        x = int(input())
        if x == 1:  # setting light flag to true
            p.light = 1
        elif x == 2:  # setting light flag to false
            p.light = 0
        else:
            colors.pr_red("Wrong input data!")
        # notes
        colors.pr_blue("Do you want to attach any additional information on patient?")
        colors.pr_green("1 - Yes")
        colors.pr_red("2 - No")
        x = int(input())
        if x == 1:  # add info
            colors.pr_blue("Enter additional info: ")
            additional_info = input()
            time = datetime.now()
            time = time.strftime("%d/%m/%Y %H:%M:%S")

            p.info = '2|' + time + '|' + additional_info+'\n'

        colors.pr_blue("Do you want to add this patient?")  # confirmation
        colors.pr_blue("Name: " + p.name + " " + p.lastName)
        colors.pr_blue("Temperature compartment: "
                       + str(p.tempMin) + "??C - " + str(p.tempMax) + "??C")
        colors.pr_blue("Humidity compartment: "
                       + str(p.humMin) + "% - " + str(p.humMax) + "%")
        if p.light == 1:
            colors.pr_blue("Light hypersensitivity: yes")
        else:
            colors.pr_blue("Light hypersensitivity: no")
        if p.info:
            colors.pr_blue("Additional information: " + p.info)
        colors.pr_green("1 - Yes")
        colors.pr_red("2 - No")
        colors.pr_yellow("3 - Enter data again")  # enter patient data again
        return p

    def add_patient(self):  # adds a patient to selected room if possible
        dbc = db_controller.DBController()  # DB Controller declaration
        while 1:
            p = self.gather_data()  # collecting input
            x = int(input())
            if x == 1:  # adding patient
                p.ID = int(self.__nextPatientID)  # generating id
                self.__nextPatientID += 1  # incrementing to next free value
                flag = 1
                while flag == 1:
                    self.show_all()
                    colors.pr_blue("Enter room number: ")
                    number = int(input())

                    for i in self.__rooms:
                        if i.get_ID() == number:
                            if i.add(p) == 1:
                                db_p = db_controller.Patient(name=p.name, surname=p.lastName, temp_max=p.tempMax,
                                                             temp_min=p.tempMin,
                                                             room=number)  # Creation of Patient for DB
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

    def relocate(self, p: patient.Patient):  # setting new room for given patient
        dbc = db_controller.DBController()  # DB Controller declaration
        flag = 1
        while flag == 1:
            while flag == 1:
                self.show_all()
                colors.pr_blue("Enter room number: ")
                number = int(input())

                for i in self.__rooms:
                    if i.get_ID() == number:
                        if i.add(p) == 1:
                            db_p = db_controller.Patient(name=p.name, surname=p.lastName, temp_max=p.tempMax,
                                                         temp_min=p.tempMin,
                                                         room=number)  # Creation of Patient for DB
                            dbc.add(db_p)  # Adding Patient into DB
                            flag = 0
                            break
                        else:
                            colors.pr_green("1 - Another room")
                            colors.pr_red("2 - Abort")
                            flag = int(input())


    def find_patient(self, option):  # displays info abut given patient
        dbc = db_controller.DBController()  # DB Controller declaration
        colors.pr_blue("Enter patient ID: ")
        patientID = int(input())
        search = 0
        for r in self.__rooms:
            if search == 1:
                break
            for p in r.get_patients():
                if patientID == p.ID:  # match
                    p.show_info()
                    print(dbc.read_patient(patientID)) # DB Controller reading patient data from db
                    colors.pr_blue("Room #" + str(r.get_ID()))
                    colors.pr_blue("Is this the right patient?")  # confirmation
                    colors.pr_green("1 - Yes")
                    colors.pr_red("2 - No")
                    x = int(input())
                    if x == 1:
                        if option == 0:  # display info
                            search = 1
                            break
                        elif option == 1:  # add note
                            colors.pr_blue("Please choose if you're entering:")
                            colors.pr_green('1 - Medical Check-up')
                            colors.pr_red('2 - Comments about the patient')
                            while True:
                                try:
                                    type=input()
                                except ValueError:
                                    colors.pr_red("Please choose correct option!")
                                    colors.pr_green('1 - Medical Check-up')
                                    colors.pr_red('2 - Comments about the patient')
                                    continue
                                if(type=='1'):
                                    colors.pr_blue('Please enter check-up type:')
                                    assesment_type = input()

                                    colors.pr_blue('Please enter check-up result:')
                                    assesment_result = input()

                                    colors.pr_blue('Do you want to add additional remarks?:')
                                    colors.pr_green('1 - Yes')
                                    colors.pr_red('2 - No')

                                    remarks_if = input()
                                    if(remarks_if=='1'):
                                        colors.pr_blue('Please enter remarks:')
                                        remarks = input()
                                    elif(remarks_if=='2'):
                                        remarks=''

                                    colors.pr_blue('Was check up taken now?:')
                                    colors.pr_green('1 - Check up was taken now (current time)')
                                    colors.pr_red('2 - I want to enter date myself')

                                    while True:
                                        try:
                                            time_if = input()
                                        except ValueError:
                                            colors.pr_red("Please choose correct option!")
                                            colors.pr_green('1 - Check up was taken now (current time)')
                                            colors.pr_red('2 - I want to enter date myself')
                                            continue
                                        if (time_if == '1'):
                                            time=datetime.now()
                                            time = time.strftime("%d/%m/%Y %H:%M:%S")
                                            break
                                        elif (time_if == '2'):
                                            colors.pr_blue('Please enter date in DD/MM/YYYY HH:MM:SS format')

                                            while True:
                                                try:
                                                    time = input()
                                                    time = datetime.strptime(time, "%d/%m/%Y %H:%M:%S")  # sprawdzenie
                                                except ValueError:
                                                    colors.pr_red('Please enter date in DD/MM/YYYY HH:MM:SS format!')
                                                    continue
                                                else:
                                                    break
                                            break
                                        else:
                                            colors.pr_red("Please choose correct option!")
                                            colors.pr_green('1 - Check up was taken now (current time)')
                                            colors.pr_red('2 - I want to enter date myself')
                                            continue

                                    output = '1|' + str(time) + '|' + assesment_type+'|'+assesment_result+'|'+remarks
                                    p.info +=output+'\n'
                                    break

                                elif(type=='2'):
                                    colors.pr_blue('Please enter additional info')
                                    additional_info=input()
                                    time = datetime.now()
                                    time = time.strftime("%d/%m/%Y %H:%M:%S")

                                    output='2|'+time+'|'+additional_info
                                    p.info+=output+'\n'
                                    break
                                else:
                                    colors.pr_red("Please choose correct option!")
                                    colors.pr_green('1 - Medical Check-up')
                                    colors.pr_red('2 - Comments about the patient')
                                    continue


                            search = 1
                            break

                        elif option == 2:  # reloacte patient
                            temp = p
                            r.get_patients().remove(p)

                            '''
                            db_p = db_controller.Patient(id=patientID ,name=p.name, surname=p.lastName, temp_max=p.tempMax,
                                                         temp_min=p.tempMin,
                                                         room=r.get_ID())  # Creation of Patient for DB
                            dbc.delete_patient(db_p)  # Deleting Patient from DB
                            '''
                            dbc.delete_patient(patientID)  # Deleting Patient from DB
                            self.relocate(temp)
                            search = 1
                            break
                    elif x == 2:
                        continue

        if search == 0:
            colors.pr_red("No patient with that ID was found.")

    def add_room(self):  # generates and adds to collection new room
        self.__rooms.append(room.Room(int(self.__nextRoomID)))
        self.__nextRoomID += 1

    def show_all(self):  # display patients allocation
        db_controller.print_rooms()
        db_controller.print_patient()
        for r in self.__rooms:
            colors.pr_cyan("|---Room #" + str(r.get_ID()) + "---|")
            r.show_patients()
            colors.pr_cyan("|-------------|")

    def show_conditions(self):  # display common ranges of factors in rooms
        for r in self.__rooms:
            colors.pr_cyan("|--------------Room #" + str(r.get_ID()) + "--------------|")
            tmin, tmax = 0, 50
            hmin, hmax = 0, 100
            light = 0
            for p in r.get_patients():
                if p.tempMin > tmin:
                    tmin = p.tempMin
                if p.tempMax < tmax:
                    tmax = p.tempMax
                if p.humMin > hmin:
                    hmin = p.humMin
                if p.humMax < hmax:
                    hmax = p.humMax
                light = p.light
            colors.pr_yellow("Temperature compartment: " + str(tmin) + "??C - " + str(tmax) + "??C")
            colors.pr_yellow("Humidity compartment: " + str(hmin) + "% - " + str(hmax) + "%")
            if light == 1:
                colors.pr_yellow("Light factor: ON")
            else:
                colors.pr_yellow("Light factor: OFF")
            colors.pr_cyan("|-----------------------------------|")
