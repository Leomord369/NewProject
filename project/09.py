import numpy as np

x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

filter1 = 20 < x
filter2 = x < 70
# and &
# or  |

print(x[filter1 & filter2])

# mask = [False, False, False, False ,False, True ,True ,False, False, False]
# print(x[mask])
# print(x>50)