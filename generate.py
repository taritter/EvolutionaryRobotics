import pyrosim.pyrosim as pyrosim


def Create_World():
    # tell pyrosim the name of the file where information about the world
    # #you're about to create should be stored
    pyrosim.Start_SDF("world.sdf")

    # stores a box with initial position x=0, y=0, z=0.5, and length, width and height all equal to 1 meter, in box.sdf
    x = 0
    y = 0
    z = 0.5

    length = 1
    width = 1
    height = 1

    length = 1
    width = 1
    height = 1
    z = 0.5
    # pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
    # pyrosim.Send_Cube(name="Box2", pos=[x,0.5,1.5] , size=[length,width,height])

    pyrosim.End()

def Create_Robot():
    #makes the body
    pyrosim.Start_URDF("body.urdf")

    # parent
    pyrosim.Send_Cube(name="Torso", pos=[1, 0, 1.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[1.5, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0.5, 0, 1])
    # child
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.End()


def Generate_Body():
    #makes the body
    pyrosim.Start_URDF("body.urdf")

    # parent
    pyrosim.Send_Cube(name="Torso", pos=[1, 0, 1.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[1.5, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0.5, 0, 1])
    # child
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.End()


def Generate_Brain():
    #makes the body
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
    pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=1.0)
    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=1, weight=1.0)
    pyrosim.End()


def main():
    Create_World()
    Create_Robot()
    Generate_Body()
    Generate_Brain()


if __name__ == "__main__":
    main()


