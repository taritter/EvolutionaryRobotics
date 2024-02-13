import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy

ITER = 1000
physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

#disables sidebars
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# add gravity
p.setGravity(0,0,-9.8)

# add floor
planeId = p.loadURDF("plane.urdf")
# blue robot body
robotId = p.loadURDF("body.urdf")


p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(ITER)
frontLegSensorValues = numpy.zeros(ITER)



for i in range(ITER):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")


	time.sleep(1/60)
	# print(i)
print(backLegSensorValues)
numpy.save("data/backLeg.npy", backLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save("data/frontLeg.npy", frontLegSensorValues, allow_pickle=True, fix_imports=True)


p.disconnect()
