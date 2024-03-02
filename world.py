import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim


class WORLD:
    def __init__(self):
        p.loadSDF("world.sdf")

