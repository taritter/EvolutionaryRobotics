import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.motors = {}
        self.motorValues = {}
        MOTOR.Prepare_To_Act(self)

    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeBack
        self.frequency = c.frequencyBack
        self.offset = c.p_o_back
        # print("joint", self.jointName)
        # print("joint type", type(self.jointName))
        if self.jointName == "Torso_FrontLeg":
            self.motorValues[self.jointName] = self.amplitude * numpy.sin(
                numpy.linspace(c.START, c.two_pi, c.ITER) * (self.frequency/2) + self.offset)
        else:
            self.motorValues[self.jointName] = self.amplitude * numpy.sin(
                numpy.linspace(c.START, c.two_pi, c.ITER) * self.frequency + self.offset)

    def Set_Value(self, robot, desiredAngle):
        #decoded_joint_name = self.jointName.decode('utf-8') if isinstance(self.jointName, bytes) else self.jointName
        #print("decoded joint in set values ", decoded_joint_name)
        self.motors[self.jointName] = pyrosim.Set_Motor_For_Joint(
            # what robot the motor is to be attached to
            bodyIndex=robot,
            # tells the simulator what joint the motor should be attached to
            jointName=self.jointName,
            # how the motor will attempt to control the motion of the joint
            controlMode=p.POSITION_CONTROL,
            # the desired angle between the two links connected by the joint
            targetPosition=desiredAngle,
            # cap the total torque ever used by a motor
            maxForce=c.force)

    def Save_Values(self):
        for i in self.motors:
            npy = "data/" + i + ".npy"
            numpy.save(npy, i, allow_pickle=True, fix_imports=True)
