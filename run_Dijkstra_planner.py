#! /usr/bin/env python

#Import the needed types 
from comp313p_planner_controller.occupancy_grid import *
from comp313p_planner_controller.DijkstraPlanner import *

#Create the occupancy grid (x, y, length)
occupancyGrid = OccupancyGrid(21, 21, 0.5)

#The cells are indexed starting from 0. 
#Set the state of the cells in the range [11,1]-[11,19] to be occupied.

for y in xrange(1, 19):
	occupancyGrid.setCell(11, y, 1)

#Define the start and goal cells
start = (3, 18)
goal = (20, 0)

#Create the planner. The first field is the title whihc will appear in the graphics window, the second the occupancy grid used

planner = DijkstraPlanner('Dijkstra Algorithm', occupancyGrid);

#This causes the planner to slow down and pause for things like key enries

planner.setRunInteractively(True)

#This specifies the height of the window drawn showing the occupancy grid. Everything should scale automatically to properly preserve the #aspect ratio

# Search and see if a path can be found. Returns True if a path from the start to the
# goal was found and False otherwise
goalReached = planner.search(start, goal)

# Extract the path. This is based on the last search carried out.
path = planner.extractPathToGoal(),

# Note that you can run multiple planners - each one will create and update its own window.
# See the minkowski_sum_tester asn an example

