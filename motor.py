import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.motors = {}
        self.motorValues = {}
        self.amplitude = c.amplitudeBack
        self.frequency = c.frequencyBack
        self.offset = c.p_o_back
        self.Prepare_To_Act()

    def Set_Value(self, robot, desiredAngle):
        # decoded_joint_name = self.jointName.decode('utf-8') if isinstance(self.jointName, bytes) else self.jointName
        # print("decoded joint in set values ", decoded_joint_name)
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

    def Prepare_To_Act(self):
        # print("joint", self.jointName)
        # print("joint type", type(self.jointName))
        if self.jointName == "Torso_FrontLeg":
            self.motorValues = self.amplitude * numpy.sin(
                numpy.linspace(c.START, c.two_pi, c.ITER) * (self.frequency / 2) + c.p_o_front)
        else:
            self.motorValues = self.amplitude * numpy.sin(
                numpy.linspace(c.START, c.two_pi, c.ITER) * self.frequency + c.p_o_back)
