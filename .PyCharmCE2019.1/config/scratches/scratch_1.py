import numpy as np
from *

x=np.random.randn(1000)
y=x+np.random.randn(1000)*0.5

plt.scatter(x,y,s=5,marker="<")            #s表示面积  Marker表示图形

plt.show()