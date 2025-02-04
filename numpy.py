

#Category	        Important Functions

#Array Creation	    np.array(), np.zeros(), np.ones(), np.arange(), np.linspace()
#Array Manipulation	np.reshape(), np.transpose(), np.concatenate()
#Math & Stats	    np.sum(), np.mean(), np.std(), np.min(), np.max(), np.argmin(), np.argmax()
#Linear Algebra	    np.dot(), np.matmul(), np.linalg.inv()
#Indexing & Slicing 	np.where(), np.argsort(), np.sort()
#Random Sampling  	np.random.seed(), np.random.rand(), np.random.choice()
#File I/O          	np.loadtxt(), np.savetxt()
#Utility	            np.unique(), np.percentile(), np.corrcoef()

# ================================== #

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]

# Create arrays of zeros/ones
zeros = np.zeros((3, 3))  
ones = np.ones((2, 2))  
print(zeros, ones)

# Create evenly spaced values
arr = np.arange(1, 10, 2)  # Start=1, Stop=10, Step=2
print(arr)  # Output: [1 3 5 7 9]

# Create specified number of points
arr = np.linspace(0, 5, 10)  # 10 evenly spaced numbers from 0 to 5
print(arr)

#Reshape without changing data
arr = np.arange(6).reshape(2, 3)  
print(arr)

#Swap rows & columns
arr = np.array([[1, 2], [3, 4]])
print(np.transpose(arr))  # Output: [[1 3] [2 4]]

#Join arrays

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concatenate((a, b)))  # Output: [1 2 3 4 5 6]

#Compute sum
arr = np.array([[1, 2], [3, 4]])
print(np.sum(arr))  # Output: 10
print(np.sum(arr, axis=0))  # Column-wise sum: [4 6]

#Compute statistical metrics
arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr))   # Output: 3.0
print(np.median(arr)) # Output: 3.0
print(np.std(arr))    # Standard deviation


# Find min/max & their indices
arr = np.array([3, 1, 5, 2])
print(np.min(arr), np.max(arr))  # Output: (1, 5)
print(np.argmin(arr), np.argmax(arr))  # Output: (1, 2)

#Dot & Matrix multiplication
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))  # Matrix multiplication
print(np.matmul(a, b))  # Preferred for 2D matrix

#Find inverse of a matrix
mat = np.array([[1, 2], [3, 4]])
inv_mat = np.linalg.inv(mat)
print(inv_mat)

#Compute percentile
arr = np.array([1, 2, 3, 4, 5])
print(np.percentile(arr, 50))  # 50th percentile (median)

#ompute correlation matrix
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
print(np.corrcoef(x, y))  # Output: [[1. 1.] [1. 1.]]

#Find indices where condition is met
arr = np.array([1, 2, 3, 4, 5])
print(np.where(arr > 3))  # Output: (array([3, 4]),)

#Generate reproducible random numbers
np.random.seed(42)
print(np.random.rand(3))  # Generates 3 random numbers

#Sort and get indices
arr = np.array([3, 1, 2])
print(np.sort(arr))  # Output: [1 2 3]
print(np.argsort(arr))  # Output: [1 2 0]

#ind unique elements
arr = np.array([1, 2, 2, 3, 4, 4])
print(np.unique(arr))  # Output: [1 2 3 4]
