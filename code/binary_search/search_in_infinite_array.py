import math

class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]

def search_in_infinite_arr(reader , key):
    start =0
    end = len(reader) -1
    if key < reader[start] or key>reader[end]:
        return -1
    while start<=end:
        mid = start + (end-start)/2
        if 



