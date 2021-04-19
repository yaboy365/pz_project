import colors


class Patient:  # patient class
    ID = None  # patient id
    name = None
    lastName = None
    tempMin, tempMax = 18.0, 22.0  # min - max temperature
    humMin, humMax = 30.0, 50.0  # min - max humidity
    light = False  # light exposure determinant
    info = None

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
            print(self.info)
