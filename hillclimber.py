import copy
import simulate
from solution import SOLUTION
import constants as c
from simulation import SIMULATION
import random

class HILL_CLIMBER:

    def __init__(self):
        self.parent = SOLUTION()


    def Evolve(self):
        self.parent.Evaluate("DIRECT")
        #self.parent.Evaluate("DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Show_Best(self):
        self.parent.Evaluate("GUI")

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        #self.child.Evaluate("GUI")
        self.Print()
        self.Select()

    def Print(self):
        print("\nPARENT FITNESS: ", self.parent.fitness)
        print("CHILD FITNESS: ", self.child.fitness)

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()


    def Select(self):
        for r in range(3):
            for col in range(2):
                if self.parent.weights[r, col] > self.child.weights[r, col]:
                    self.parent = self.child
                    #print("parent did worse, switched")

