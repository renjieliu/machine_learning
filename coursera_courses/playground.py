from xml.sax.handler import property_interning_dict
import numpy as np;

arr1 = np.array([_ for _ in range(100000)])
arr2 = np.array([_ for _ in range(100000)])
print(np.dot(arr1, arr2))

arr1 = np.zeros(4, None)
print(arr1)


arr2 = np.random.random_sample(4)
arr3 = np.array([1000000] * 4)
print(np.dot(arr2, arr3))

print(arr2.shape)




