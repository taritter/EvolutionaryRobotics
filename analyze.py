import numpy
import matplotlib.pyplot

#back = numpy.load("data/backLeg.npy")
#front = numpy.load("data/frontLeg.npy")
angle_back = numpy.load("data/targetAngleBack.npy")
angle_front = numpy.load("data/targetAngleFront.npy")


#matplotlib.pyplot.plot(back, label='Back Leg', linewidth=2)
#matplotlib.pyplot.plot(front, label='Front Leg', linewidth=2)
matplotlib.pyplot.plot(angle_back, label='Back Angle', linewidth=6)
matplotlib.pyplot.plot(angle_front, label='Front Angle', linewidth=2)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()



