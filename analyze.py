import numpy
import matplotlib.pyplot

back = numpy.load("data/backLeg.npy")
front = numpy.load("data/frontLeg.npy")

matplotlib.pyplot.plot(back, label='Back Leg', linewidth=2)
matplotlib.pyplot.plot(front, label='Front Leg', linewidth=2)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()



