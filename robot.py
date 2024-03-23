from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self):
        # add floor
        self.planeId = p.loadURDF("plane.urdf")
        # blue robot body
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)
        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
        # print("this is self.sensors ", self.sensors)


    def Sense(self, timeStep):
        for i in self.sensors:
            SENSOR.values = self.sensors[i].Get_Value(timeStep)
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:

            try:
                decoded_joint_name = jointName.decode('utf-8')
            except UnicodeDecodeError:
                decoded_joint_name = str(jointName)
            self.motors[decoded_joint_name] = MOTOR(decoded_joint_name)

    def Act(self, time):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                self.jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                self.desiredAngle = self.nn.Get_Value_Of(neuronName)
                print("desired angle ", self.desiredAngle)
                self.motors[self.jointName].Set_Value(self.robotId, time)
                print("neuron name ", neuronName)
                print("joint name ", self.jointName)



    def Think(self):
        self.nn.Update()
        self.nn.Print()


    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        print(stateOfLinkZero)
        positionOfLinkZero = stateOfLinkZero[0]
        print(positionOfLinkZero)
        xCoordinateOfLinkZero = str(positionOfLinkZero[0])
        f = open("fitness.txt", 'a')
        f.write(xCoordinateOfLinkZero + "\n")
        f.close()

