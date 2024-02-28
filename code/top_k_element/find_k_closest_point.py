from __future__ import print_function

from heapq import *

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()
    

    def distance_from_origin(self):
        return (self.x*self.x) + (self.y*self.y)
    
    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

def find_closest_point(points,k):
    maxHeap = []
    for i in range(k):
        heappush(maxHeap, points[i])

    for i in range(k,len(points)):
        if points[i].distance_from_origin()< maxHeap[0].distance_from_origin():
            heappop(maxHeap)
            heappush(maxHeap,points[i])
    return maxHeap



def main():
  result = find_closest_point([Point(1, 3), Point(3, 4), Point(2, -1)], 1)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()
            

# Time Complexity - O(N*logK)

# Space Compexity - O(K)

    
