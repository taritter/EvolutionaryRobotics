import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random

import simulate


class SOLUTION:

    def __init__(self):
        self.weights = np.random.rand(3, 2) * 2 - 1
        print(self.weights)

    def Evaluate(self, directOrGUI):
        self.Create_Brain()
        if directOrGUI == "DIRECT":
            os.system("python3 simulate.py DIRECT")
        else:
            os.system("python3 simulate.py GUI")
        with open("fitness.txt", 'r') as f:
            self.fitness = float(f.read())
        f.close()
    def Create_World(self):
        pass

    def Create_Body(self):
        pass

    def Mutate(self):
        randomColumn = random.randint(0, 1)
        randomRow = random.randint(0, 2)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

