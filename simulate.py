import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import math
import random

ITER = 1000
physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

#disables sidebars
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# add gravity
p.setGravity(0, 0, -9.8)

# add floor
planeId = p.loadURDF("plane.urdf")
# blue robot body
robotId = p.loadURDF("body.urdf")

amplitudeBack = numpy.pi/4
amplitudeFront = numpy.pi/10
frequencyBack = 6
frequencyFront = 2
phaseOffsetFront = numpy.pi/4
phaseOffsetBack = numpy.pi/20


p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(ITER)
frontLegSensorValues = numpy.zeros(ITER)

targetAngleBack = numpy.sin(numpy.linspace(0, (2*numpy.pi), ITER))*(numpy.pi/4)
targetAngleFront = numpy.sin(numpy.linspace(0, (2*numpy.pi), ITER))*(numpy.pi/4)


for i in range(ITER):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

	targetAngleBack = amplitudeBack * numpy.sin(numpy.linspace(0, (2*numpy.pi), ITER) * frequencyBack + phaseOffsetBack)
	targetAngleFront = amplitudeFront * numpy.sin(numpy.linspace(0, (2*numpy.pi), ITER) * frequencyFront + phaseOffsetFront)


	pyrosim.Set_Motor_For_Joint(
		# what robot the motor is to be attached to
		bodyIndex=robotId,
		# tells the simulator what joint the motor should be attached to
		jointName=b'Torso_BackLeg',
		# how the motor will attempt to control the motion of the joint
		controlMode=p.POSITION_CONTROL,
		# the desired angle between the two links connected by the joint
		targetPosition=targetAngleBack[i],
		# cap the total torque ever used by a motor
		maxForce=200)

	pyrosim.Set_Motor_For_Joint(
		# what robot the motor is to be attached to
		bodyIndex=robotId,
		# tells the simulator what joint the motor should be attached to
		jointName=b'Torso_FrontLeg',
		# how the motor will attempt to control the motion of the joint
		controlMode=p.POSITION_CONTROL,
		# the desired angle between the two links connected by the joint
		targetPosition=targetAngleFront[i],
		# cap the total torque ever used by a motor
		maxForce=200)

	time.sleep(1/100)
	# print(i)
print(backLegSensorValues)
numpy.save("data/backLeg.npy", backLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save("data/frontLeg.npy", frontLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save("data/targetAngleBack.npy", targetAngleBack, allow_pickle=True, fix_imports=True)
numpy.save("data/targetAngleFront.npy", targetAngleFront, allow_pickle=True, fix_imports=True)




p.disconnect()
