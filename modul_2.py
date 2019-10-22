import math
from const import g
V=math.sqrt(g*100*math.tan(0.52**2)/2*math.cos((math.pi/3)**2)*(1-math.tan(0.52)*math.tan(math.pi/3)))
print(V)