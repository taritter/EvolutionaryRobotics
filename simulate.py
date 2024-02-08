import pybullet as p
import time
import pybullet_data

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

for i in range(1000):
	p.stepSimulation()
	time.sleep(1/60)
	print(i)

p.disconnect()