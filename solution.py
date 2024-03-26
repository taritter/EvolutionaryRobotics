import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time


class SOLUTION:

    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = np.random.rand(3, 2) * 2 - 1
        print(self.weights)

    def Evaluate(self):
        pass

    def Wait_For_Simulation_To_End(self):
        #print("SELF ID", self.myID)
        fitness_file = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitness_file):
            time.sleep(0.01)

        with open(fitness_file, 'r') as f:
            self.fitness = float(f.read())
            # print("\nSTORED FITNESS IN WAIT FOR SIMULATION TO END", self.fitness)
        f.close()
        os.system("del " + fitness_file)

    def Start_Simulation(self, directOrGUI):
        self.Create_Brain()
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID))

    def Set_ID(self):
        self.myID += 1

    def Create_World(self):
        pass

    def Create_Body(self):
        pass

    def Mutate(self):
        randomColumn = random.randint(0, 1)
        randomRow = random.randint(0, 2)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

