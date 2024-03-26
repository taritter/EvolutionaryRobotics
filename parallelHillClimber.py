import copy
from solution import SOLUTION
import constants as c
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        count_id = 0
        brain_file = f"brain{count_id}.nndf"
        while not os.path.exists(brain_file):
            count_id += 1
            brain_file = f"brain{count_id}.nndf"
            if count_id > 25:
                break
        try:
            os.remove(brain_file)
            print(f"{brain_file} has been deleted.")
        except FileNotFoundError:
            print(f"{brain_file} does not exist.")
        except Exception as e:
            print(f"Error occurred while deleting {brain_file}: {e}")

        count_id = 0
        fitness_file = f"fitness{count_id}.txt"
        while not os.path.exists(fitness_file):
            count_id += 1
            fitness_file = f"fitness{count_id}.txt"
            if count_id > 25:
                break
        try:
            os.remove(fitness_file)
            print(f"{fitness_file} has been deleted.")
        except FileNotFoundError:
            print(f"{fitness_file} does not exist.")
        except Exception as e:
            print(f"Error occurred while deleting {fitness_file}: {e}")

        self.parents = {}
        self.nextAvailableID = 0
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Show_Best(self):
        lowest = 10
        low_parent = self.parents[0]
        for p in self.parents.values():
            if p.fitness < lowest:
                lowest = p.fitness
                low_parent = p
        print("LOWEST", lowest)
        low_parent.Start_Simulation("GUI")

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Evaluate(self, solutions):
        for p in solutions.values():
            p.Start_Simulation("DIRECT")
        for p in solutions.values():
            p.Wait_For_Simulation_To_End()

    def Print(self):
        print("\n")
        for parent, child in zip(self.parents.values(), self.children.values()):
            print(f"\nPARENT FITNESS: {parent.fitness} CHILD FITNESS {child.fitness}")
        print("\n")

    def Spawn(self):
        self.children = {}
        count = 0
        for parent in self.parents.values():
            self.children[count] = copy.deepcopy(parent)
            SOLUTION.Set_ID(self.children[count])
            count += 1

    def Mutate(self):
        for child in self.children.values():
            child.Mutate()


    def Select(self):
        num_parent = len(self.parents)
        for i in range(num_parent):
            for r in range(3):
                for col in range(2):
                    if self.parents[i].weights[r, col] > self.children[i].weights[r, col]:
                        self.parents[i + 1] = self.children[i]


