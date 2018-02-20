#! /usr/bin/env python

# this file contains the planner for Best-First Algorithm or Greedy Algorithm, it is based on the general forward search algorithm

from cell_based_forward_search import CellBasedForwardSearch
from Queue import PriorityQueue
import math

#create the self class that implements Greedy forward Search Algorithm

class ShortestDistanceFirstPlanner(CellBasedForwardSearch):

    # self order the cells on a priority queue, sorted in terms of distance to target: shorter is better
    
    def __init__(self, title, occupancyGrid):
        CellBasedForwardSearch.__init__(self, title, occupancyGrid)
        self.priorityQueue = PriorityQueue()

    # Sort in order of distance from the target and use that
    def pushCellOntoQueue(self, cell):

        # We compute the squared Euclidean distance to the goal
        dX = cell.coords[0] - self.goal.coords[0]
        dY = cell.coords[1] - self.goal.coords[1]
        d = dX * dX + dY * dY
        
        self.priorityQueue.put((d, cell))

    # Check the queue size is zero
    def isQueueEmpty(self):
        return self.priorityQueue.empty()

    # Simply pull from the front of the list
    def popCellFromQueue(self):
        tuple = self.priorityQueue.get()
        return tuple[1]

    def resolveDuplicate(self, cell, parentCell):
        # Nothing to do in self case
        pass
