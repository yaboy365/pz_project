import re

import colors


class Patient:  # patient class
    ID = None  # patient id
    name = None
    lastName = None
    tempMin, tempMax = 18.0, 22.0  # min - max temperature
    humMin, humMax = 30.0, 50.0  # min - max humidity
    light = False  # light exposure determinant
    info = ''

    def show_additional_info(self):
        info = re.split("\n", self.info)
        for info_2 in info:
            info_3 = re.split("\|", info_2)
            if(info_3[0]=='1'):
                print('Date: '+info_3[1]+' Medical check-up: '+info_3[2]+' Result: '+info_3[3])
                if(info_3[4]!=''):
                    print('         Additional remarks: '+info_3[4])
            elif (info_3[0] == '2'):
                print('Date: '+info_3[1]+' Additional info: '+info_3[2])


    def show_info(self):  # display patient information
        colors.pr_blue("Name: " + self.name + " " + self.lastName)
        colors.pr_blue("Temperature compartment: "
                       + str(self.tempMin) + "°C - " + str(self.tempMax) + "°C")
        colors.pr_blue("Humidity compartment: "
                       + str(self.humMin) + "% - " + str(self.humMax) + "%")
        if self.light == 1:
            colors.pr_blue("Light hypersensitivity: yes")
        else:
            colors.pr_blue("Light hypersensitivity: no")
        if self.info:
            colors.pr_blue("Additional information:")
            self.show_additional_info()

