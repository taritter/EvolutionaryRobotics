import copy

import simulate
from solution import SOLUTION
import constants as c
import random

class HILL_CLIMBER:

    def __init__(self):
        self.parent = SOLUTION()



    def Evolve(self):
        self.parent.Evaluate(simulate.directOrGUI)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Show_Best(self):
        simulate.directOrGUI = "GUI"

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(simulate.directOrGUI)
        self.Print()
        self.Select()

    def Print(self):
        print(f"parent: {self.parent.weights} child: {self.child.weights}")

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        print(self.parent.weights)
        print(self.child.weights)

    def Select(self):
        print(self.parent.weights)
        print(self.child.weights)
        for r in range(3):
            for col in range(2):
                if self.parent.weights[r, col] > self.child.weights[r, col]:
                    self.parent = self.child
                    print("parent did worse, switched")

