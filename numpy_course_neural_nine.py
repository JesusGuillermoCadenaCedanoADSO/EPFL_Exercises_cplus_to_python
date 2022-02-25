#NumPy Full Python Course - Data Science Fundamentals
#https://www.youtube.com/
#watch?v=4c_mwnYdbhQ&list=PLDobAhKPyFshEq3wYrUXp7KAzP_xnIiAu&index=17&t=5s

import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(type(a))

a_mul = np.array([[[1, 2, 3, 1], 
                   [4, 5, 6, 1], 
                   [7, 8, 9, 1]], 
                  [[1, 1, 1, 1], 
                   [1, 1, 1, 1], 
                   [1, 1, 1, 1]]])
print(a_mul.shape)
print(a_mul.ndim)
print(a_mul.size)
print(a_mul.dtype)

b = np.array([1, "c", 2])
print(b.dtype)

c = np.array([1, "5", 2], dtype=np.int32)
print(c.dtype)

d = {1: 0}

e = np.array([1, d])
print(e.dtype)

#filling arrays
print("\nfilling arrays\n")
f = np.full((2, 3, 4), 7)
print(f)

g = np.zeros((2, 3, 4))
print(g)

h = np.empty((2, 2))
print()
print(h)

x_values = np.arange(0, 33, 3)
print(x_values)

y_values = np.linspace(1, 10, 10)
print(y_values)

#nan is used to fill missing values of a matrix
print(np.isnan(np.nan))
#print(np.isnan(np.sqrt(-1)))
#print((np.sqrt(-1)))
#inf is used to fill a value of a division by zero instead of throw an exception
#print(np.isinf(np.inf))
#print((np.array([10])/0))

#mathematical operations
print("\nmathematical operations\n")
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 0]

a1 = np.array(l1)
a2 = np.array(l2)

print(l1 * 5)
print(a1 * 5)
print(a1 + a2)

a3 = np.array([1, 2, 3])
a4 = np.array([[1], [2]])

print(a3 + a4)

a5 = np.array([[1, 2, 3], [4, 5, 6]])

print(np.sqrt(a5))

#array methods
print("\narray methods\n")
a6 = np.array([1, 2, 3])

print(np.append(a6, [7, 8, 9]))
print(a6)

print(np.insert(a6, 3, [4, 5, 6]))

a7 = np.array([[1, 2, 3], [4, 5, 6]])

print(np.delete(a7, 1))
print(np.delete(a7, 3))
print(np.delete(a7, 4))
print(np.delete(a7, 1, 0))
print(np.delete(a7, 1, 1))
print(np.delete(a7, 0, 0))
print(np.delete(a7, 0, 1))
print(np.delete(a7, -1, 1))

print("\nsort arrays\n")
dtype = [('name', 'S10'), ('height', float), ('age', int)]
values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38),
          ('Galahad', 1.7, 38)]
unsorted = np.array(values, dtype=dtype)
sorted = np.sort(unsorted, order='height')
print("unsorted\n", unsorted)
print("\nsorted by height (name, height, age) ascending\n", sorted)

a_unsorted = np.random.randint(1, 10, 10)
print("a_unsorted\n", a_unsorted)

a_sorted_ascending = np.sort(a_unsorted)
print("a_sorted_ascending\n", a_sorted_ascending)

a_sorted_descending = np.sort(a_unsorted)[::-1]
print("a_sorted_descending\n", a_sorted_descending)



#structural methods
print("\nstructural methods\n")
a8 = np.array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20]])

print(a8.shape)
print(a8.reshape((5, 4)))
print(a8.reshape((20, )))
print(a8.reshape((20, 1)))
print(a8.reshape((2, 10)))
print(a8.reshape((2, 2, 5)))
a8.resize(10, 2)
print((a8))

#ravel returns a refference to the original array
var1 = a8.ravel()
var1[2] = 100
print(var1)
print("after ravel\n", a8)
#flatten returns a copy of the original array
a8 = np.array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20]])
var1 = a8.flatten()
var1[2] = 100
print(var1)
print("after flatten\n", a8)

var2 = [v for v in a8.flat]
print(var2)

print(a8.transpose())
print()
#swapaxes: interchange two axes of an array
print(a8.swapaxes(0, 1))


#concatenating, stacking, splitting
print("\nconcatenating, stacking, splitting\n")

a9 = np.array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10]])

a10 = np.array([[11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20]])

a = np.concatenate((a9, a10), axis=0)
print(a)
print()
a = np.concatenate((a9, a10), axis=1)
print(a)
print()
a = np.stack((a9, a10))
print(a)
print(a.shape)
print("vstack\n")
a = np.vstack((a9, a10))
print(a)
print(a.shape)
print("hstack\n")
a = np.hstack((a9, a10))
print(a)
print(a.shape)


a8 = np.array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20]])

print("split\n")
print(np.split(a8, 2, axis=0))

a9 = np.array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20]])

print()
print(np.split(a9, 4, axis=0))

a10 = np.array([[1, 2, 3, 4, 5, 6],
               [7, 8, 9, 10, 11, 12],
               [13, 14, 15, 16, 17, 18],
               [18, 19, 20, 21, 22, 23]])

print()
print(np.split(a10, 3, axis=1))

#agregate functions
print("\nagregate functions\n")

print("max :", a10.max())
print("mean :", a10.mean())
print("standard deviation :", a10.std())
print("sum :", a10.sum())
print("median :", np.median(a10))

#random
print("\nrandom\n")

number = np.random.randint(100)
print(number)
print()
numbers = np.random.randint(90, 100, size=(2, 3, 4))
print(numbers)
print()

numbers = np.random.binomial(10, p=0.5, size=(5, 10))
print(numbers)
print()

numbers = np.random.normal(loc=170, scale=15, size=(5, 10))
print(numbers)

numbers = np.random.choice([10, 20, 30, 40, 50], size=(5, 10))
print(numbers)

#exporting and importing
print("\nexporting and importing\n")

#exporting
#np.save("myarray.npy", a10)

#importing
#a = np.load("myarray.npy")
#print(a)

np.savetxt("myarray.csv", a10, delimiter=",")

a = np.loadtxt("myarray.csv", delimiter=",")
print(a)




