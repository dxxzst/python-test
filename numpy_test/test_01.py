import numpy as np

raw_data = [1, 2.3, 4, 6.0]
arr1 = np.array(raw_data)
print(arr1, type(arr1), arr1.dtype)

arr2 = arr1.astype(np.int32)
print(arr2, type(arr2), arr2.dtype)

arr3 = np.arange(0, 10, 2, np.int32)
print(arr3, type(arr3), arr3.dtype)

arr4 = np.linspace(0, 20, 50)
print(type(arr4), arr4)

arr5 = np.zeros(shape=(3, 4))  # arr6 = np.zeros(shape=[3, 4])
print(arr5)
print("维度：", arr5.ndim)
print("shape：", arr5.shape)

arr6 = np.arange(15)
print(arr6)
arr6 = arr6.reshape(3, 5)
print(arr6)

arr7 = np.ones_like(arr6)
print(arr7)

print(arr6 + arr7)
print(np.multiply(arr6, arr7))
