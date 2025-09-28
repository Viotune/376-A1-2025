import numpy as np
import roboticstoolbox as rtb
from spatialmath import *
from math import pi
import matplotlib.pyplot as plt
from matplotlib import cm
np.set_printoptions(linewidth=100, formatter={'float': lambda x: f"{x:8.4g}" if abs(x) > 1e-10 else f"{0:8.4g}"})

%matplotlib widget

# Moved code from practical 3 over

panda = rtb.models.DH.Panda()

print(panda)

panda.fkine(panda.qr)

T = panda.fkine_all(panda.qr)
print(T)

robot = rtb.DHRobot(
    [   
        # rtb.PrismaticDH(...) prismatic joint
        rtb.RevoluteDH(alpha=pi/2), # Rev joint
        rtb.RevoluteDH(a=0.5),
        rtb.RevoluteDH(d=0.1, a=0.04, alpha=pi/2),
        rtb.RevoluteDH(d=0.4, alpha=-pi/2),
        rtb.RevoluteDH(alpha=pi/2),
        rtb.RevoluteDH()
    ], name="myRobot")

q=[0, 0, 0, 0, 0, 0]
robot.fkine(q)

robot.plot(q) # drag on plot to render robot