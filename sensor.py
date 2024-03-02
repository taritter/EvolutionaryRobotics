import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.ITER)

    def Get_Value(self, timeStep):
        self.values[timeStep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)


    def Save_Values(self):
        for i in self.linkName:
            npy = "data/" + i + ".npy"
            numpy.save(npy, i, allow_pickle=True, fix_imports=True)

