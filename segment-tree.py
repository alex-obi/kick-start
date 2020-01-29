import numpy as np
import math

# Class definition
##################
class SegmentTree():

    def __init__(self, array, query_fun):
        self.query_fun = query_fun
        try:
            t = len(query_fun(None))
        except:
            t = 1
        self.array = array
        self.n = len(array)
        self.n_nodes = 2 * self.n - 1
        self.height = math.ceil(math.log2(self.n))
        self.size = 2 ** (self.height + 1) - 1;
        self.st = np.empty((self.size, t), dtype=int)
        self._build(0, self.n - 1, 0)

    def _center(self, sx, ex):
        return sx + (ex - sx) // 2;

    def _build(self, sx, ex, i):
        if sx == ex:
            self.st[i] = self.array[sx]
            return self.query_fun(self.st[i])
        else:
            c = self._center(sx, ex)
            self.st[i] = self.query_fun(self._build(sx, c, i * 2 + 1),
                                        self._build(c + 1, ex, i * 2 + 2))
            return self.st[i]

    def _query(self, l, r, sx, ex, i):
        if l <= sx and r >= ex:
            # Segment is full part of query
            return self.query_fun(self.st[i])
        elif l > ex or r < sx:
            # No intersection
            return self.query_fun(None)
        else:
            c = self._center(sx, ex)
            return self.query_fun(self._query(l, r, sx, c, 2 * i + 1),
                                  self._query(l, r, c + 1, ex, 2 * i + 2))

    def query(self, l, r):
        return self._query(l, r, 0, self.n - 1, 0)

# Query functions to run queries
################################

def minmax_fun(x, y=None):
    if x is None:
        # Empty case
        return (np.iinfo(int).max, 0)
    elif y is None:
        # Single case
        return (x[0], x[1])
    else:
        # Double case
        return (min(x[0], y[0]), max(x[1], y[1]))

def min_fun(x, y=None):
    if x is None:
        # Empty case
        return np.iinfo(st.st[0].dtype).max
    elif y is None:
        # Single case
        return x
    else:
        # Double case
        return min(x, y)

# Test code
###########

x = [1, 4, 9, 8, 7, 2, 3, 5, 6]
l, r = 2, 6
print("Array:", x)
st = SegmentTree(x, minmax_fun)
min, max = st.query(l, r)
print("Min:", min, "Max:", max)
print("for bounds of [{},{}]".format(l, r))
