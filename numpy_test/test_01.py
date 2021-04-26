import numpy as np

raw_data = [1, 2.3, 4, 6.0]
arr1 = np.array(raw_data)
print(arr1, arr1.dtype)

arr2 = arr1.astype(np.int32)
print(arr2, arr2.dtype)
