#!/usr/bin/env python

from heapq import heappush, heappop

class Node(object):
    
    def __init__(self, i, d):
        self.i = i
        self.d = d
    
    def __cmp__(self, obj): 
        return cmp(self.d, obj.d)
    
def dijkstra(src, graph):
    
    n = len(graph)
    dist = [-1] * n
    heap = []
    heappush(heap, Node(src, 0))
    
    while not len(heap) == 0:
        node = heappop(heap)
    
        if dist[node.i] >= 0: 
            continue
        dist[node.i] = node.d
        
        for i in range(n):
            if i == node.i: 
                continue
            if graph[node.i][i] >= 0:
                heappush(heap, Node(i, node.d + graph[node.i][i]))
    return dist

if __name__ == '__main__':
    
    graph = [[0, 7, 9, -1, -1, 14],
             [7, 0, 10, 15, -1, -1],
             [9, 10, 0, 11, -1, 2],
             [-1, 15, 11, 0, 6, -1],
             [-1, -1, -1, 6, 0, 9],
             [14, -1, 2, -1, 9, 0]]
    
    print dijkstra(0, graph)
