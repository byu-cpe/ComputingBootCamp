import numpy as np

##########################
# Numpy Array Creation
a = np.array([0, 1, 2])
print(a)

b = np.array([[0,1], [2,3]])
print(b)

c = np.zeros([1, 2])
print(c)

d = np.full([3, 2], 3.0)
print(d)

e = np.arange(0, 10)
print(e)

f = np.linspace(0.0, 1.0, 20)
print(f)

#########################
# Index into array
print(f[0:2])
print(f[-5:len(f)])
print(f[0:10:2])

#########################
# operations on arrays

# Operations applied to each element
print(f - 1)

print(a)
print(a**2)



# Operations on arrays
h = np.array([3, 5, 1, 2, 7, 3, 8])
print(h)
print(np.sort(h))
print(np.unique(h)) # Sorts too
print(sum(h))

# List like...
# Check if contains
print(5 in h)

# List comprehension
g = [x**2 for x in h if x % 2 == 0]
print(g)

############################
# Linear Algebra Operations

i = np.identity(2)*2
print(i)

j = np.random.rand(2, 2)
print(j)

# Matrix  Multiplication
k = np.matmul(i, j) # Standard Matrix Multiply
print(k)
print(i * j) # Element wise

# trace, diag
print(np.trace(k))
print(np.diag(k))

# matrix inverse
print(np.linalg.inv(i))

# eigenvalue decomposition
w, v = np.linalg.eig(b)
print(w)
print(v)

w, v = np.linalg.eig(i)
print(w)
print(v)
