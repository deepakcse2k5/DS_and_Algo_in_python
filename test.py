import numpy as np

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def single_linkage_similarity(cluster1, cluster2):
    min_distance = float('inf')
    for point1 in cluster1:
        for point2 in cluster2:
            distance = euclidean_distance(point1, point2)
            if distance < min_distance:
                min_distance = distance
    similarity = 1 / min_distance
    return similarity

cluster1 = [(10,2), (4,15), (0,15), (3,12), (7,8), (4,8)]
cluster2 = [(-1,-5), (-8,-10), (-10,-20), (-4,-20), (-1,-25)]

similarity = single_linkage_similarity(cluster1, cluster2)
print("Similarity between the two clusters using Single Linkage algorithm:", similarity)
