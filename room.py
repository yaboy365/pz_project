import colors
import patient


class Room:  # room class
    def __init__(self, ID):
        self.__ID = ID  # room id
        self.__patients = []  # patients in room
        self.__MAX_SIZE = 3  # room max size

    def getID(self):
        return self.__ID

    def getPatients(self):
        return self.__patients

    def add(self, p: patient.Patient):  # adds a patient to room or tells if that's not possible
        if len(self.__patients) == 0:
            self.__patients.append(p)
            colors.prGreen("Patient safely added into room #" + str(self.__ID) + ".")
            return 1
        elif len(self.__patients) >= self.__MAX_SIZE:
            colors.prRed("Room full!")
            return 0
        else:
            flag = 0
            for i in self.__patients:
                if p.tempMax < i.tempMin or p.tempMin > i.tempMax:
                    flag = 1
                    break
            if flag == 0:
                self.__patients.append(p)
                colors.prGreen("Patient safely added into room #" + str(self.__ID) + ".")
                return 1
            elif flag == 1:
                colors.prRed("Temperature conflict between patients!")
                return 0

    def showPatients(self):  # shows patients in room
        for p in self.__patients:
            print(p.name, p.lastName)
