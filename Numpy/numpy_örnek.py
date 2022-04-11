from typing_extensions import OrderedDict
import numpy as np

np_first = np.random.randint(5,1000,10)
np_second = np.random.randint(1000,10000,20)

even_first = np_first %2 == 0
odd_second = np_second %2 == 1

# print(even_first, "\n\n\n")
print(np_first , "\n" , np_second, "\n\n\n")
print(np_first[even_first], "\n" , np_second[odd_second])