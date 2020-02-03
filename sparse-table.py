# Adaption of https://www.geeksforgeeks.org/sparse-table/

import numpy as np
import math

# Class definition
##################
class SparseTable():

    def __init__(self, array, query_fun):
        n = len(array)
        self.query_fun = query_fun
        self.mem = np.empty((n, math.ceil(math.log2(n))), dtype=int)
        self.mem[:, 0] = array
        j = 1 # 2**j is size of interval
        while (1 << j) <= n:
            i = 0 # start index of interval
            while (i + (1 << j) - 1) < n:
                self.mem[i, j] = self.query_fun(self.mem[i, j-1], self.mem[i + (1 << (j-1)), j-1])
                i += 1
            j+= 1

    def query(self, l, r):
        j = int(math.log2(r - l + 1))
        return self.query_fun(self.mem[l, j], self.mem[r - (1 << j) + 1, j])

# Query functions to run queries
################################

def min_fun(x, y):
    return min(x, y)

def closest_to_10(x, y):
    if abs(10 - x) < abs(10 - y):
        return x
    else:
        return y

# Test code
###########

x = [7, 2, 3, 0, 5, 10, 3, 12, 18]
print("Array:", x)
st = SparseTable(x, min_fun)
print("min(0, 4):", st.query(0, 4))  
print("min(4, 7):", st.query(4, 7))  
print("min(7, 8):", st.query(7, 8))
st = SparseTable(x, max)
print("max(0, 4):", st.query(0, 4))  
print("max(4, 7):", st.query(4, 7))  
print("max(7, 8):", st.query(7, 8))
st = SparseTable(x, closest_to_10)
print("closest10(0, 4):", st.query(0, 4))  
print("closest10(4, 7):", st.query(4, 7))  
print("closest10(7, 8):", st.query(7, 8))
