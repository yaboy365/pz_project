import colors
import patient


class Room:  # room class
    def __init__(self, ID):
        self.__ID = ID  # room id
        self.__patients = []  # patients in room
        self.__MAX_SIZE = 3  # room max size

    def get_ID(self):
        return self.__ID

    def get_patients(self):
        return self.__patients

    def add(self, p: patient.Patient):  # adds a patient to room or tells if that's not possible
        if len(self.__patients) == 0:
            self.__patients.append(p)
            colors.pr_green("Patient safely added into room #" + str(self.__ID) + ".")
            return 1
        elif len(self.__patients) >= self.__MAX_SIZE:
            colors.pr_red("Room full!")
            return 0
        else:
            flag = 0
            for i in self.__patients:
                if (p.tempMax < i.tempMin or p.tempMin > i.tempMax
                        or p.humMax < i.humMin or p.humMin > i.humMax
                        or p.light != i.light):
                    flag = 1
                break
        if flag == 0:
            self.__patients.append(p)
            colors.pr_green("Patient safely added into room #" + str(self.__ID) + ".")
            return 1
        elif flag == 1:
            colors.pr_red("Health conflict between patients!")
            return 0

    def show_patients(self):  # shows patients in room
        for p in self.__patients:
            print(p.name, p.lastName)
