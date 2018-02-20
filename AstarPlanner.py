#!/usr/bin/env python

# this file contains the planner for Dijsktra's algorithm, it is based on the general forward search algorithm

#import packages and external files
from DijkstraPlanner import *
import math

# self class implements the A* search algorithm

class AStarPlanner(DijkstraPlanner):
   
    def __init__(self, title, occupancyGrid):
	self.heuristic = 'constant'
        DijkstraPlanner.__init__(self, title, occupancyGrid)

    # Update the cost to self cell and sort according to self cumulative cost
    def pushCellOntoQueue(self, cell):

        # Work out the cost of the action from the parent to self cell
        # which defines the cost so far
        if (cell.parent is not None):
            dX = cell.coords[0] - cell.parent.coords[0]
            dY = cell.coords[1] - cell.parent.coords[1]
            d = math.hypot(dX,dY)
            cell.pathCost = cell.parent.pathCost + d
        else:
            cell.pathCost = 0

        # Compute the cost-to-go using the configuration space distance
        # We compute the squared Euclidean distance to the goal
	dX = cell.coords[0] - self.goal.coords[0]
	dY = cell.coords[1] - self.goal.coords[1]
	if self.heuristic == 'euclidian':
		G = math.hypot(dX,dY)
	elif self.heuristic == 'zero':
		G = 0
	elif self.heuristic == 'manhattan':
		G = dX+dY
	elif self.heuristic == 'octile':
		G = dX + dY + (math.sqrt(2)-2)*min(dX,dY)
	elif self.heuristic == 'constant':
		G = 5
        #dXG = cell.coords[0] - self.goal.coords[0]
        #dYG = cell.coords[1] - self.goal.coords[1]
        #G = math.sqrt(dXG * dXG + dYG * dYG)
        #G = abs(dXG) + abs(dYG)
        #G = 0
        cost = cell.pathCost + G
        
        self.priorityQueue.put((cost, cell))
