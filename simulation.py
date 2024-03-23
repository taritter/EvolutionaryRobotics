import simulate
from world import WORLD
from robot import ROBOT
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time


class SIMULATION:
    def __init__(self):
        if simulate.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.linkName = {}
        # disables sidebars
        # p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        self.robot = ROBOT()
        # add gravity
        p.setGravity(c.START, c.START, c.GRAVITY)
        self.world = WORLD()


    def Run(self):


        for i in range(c.ITER):
            print(i)
            p.stepSimulation()
            ROBOT.Sense(self.robot, i)
            self.robot.Think()
            ROBOT.Act(self.robot, i)
            time.sleep(1 / 300)


    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()

