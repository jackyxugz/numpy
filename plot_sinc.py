import numpy as np
from matplotlib.pyplot import plot, show, imshow

x = np.linspace(0, 4, 100)
vals = np.sinc(x)
plot(x, vals)
show()

y = np.linspace(0, 4, 100)
yy = np.outer(y, y)
vals1 = np.sinc(yy)
imshow(vals1)
show()