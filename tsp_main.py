# -*- coding: utf-8 -*-
"""
Project main file. 

@author: Pavel, Cristina-Maria, 11807972
        
"""

# Import your modules here.
import tsp_construct_heuristics as c
import tsp_localsearch_heuristics as ls
import tsp_read_data as read

import plot
import utils

import random
import time
# End import section.


# Main program.

# These are the instances you should be able to solve in the end.
instances = ['burma14.tsp', 'bays29.tsp', 'berlin52.tsp', 'bier127.tsp']
optima = {'burma14.tsp':3323, 'bays29.tsp':2020, 'berlin52.tsp':7542, 'bier127.tsp':118282}

# You can begin by solving the smallest one, and then try the rest when the code is working
# Comment the next line if you want to try all instances
instances = [instances[1]]

for instance in instances:
    print('\nSolving instance:', instance)

    # First, read instance data using the function in project_read_data.
    coordinates, matrix = read.read_instance(instance)
    
    # (Measure optimization time)
    start = time.time()
    
    # Second, build a solution to the TSP
    route = c.make_dummy_route(matrix)
    total_time = time.time() - start

    # print(route)
    cost = utils.calc_cost(route, matrix)
    
    # Third, improve that solution by using a local search
    start = time.time()
    new_route,new_cost = ls.make_dummy_ls(route, matrix)
    total_time += time.time() - start
    
   
    
    # Some printing now
    print('Cost of the initial solution:', cost)
    print('Cost after optimization     :', new_cost, "(", optima[instance], ")")
    print('Total time                  :', total_time)
    
    #plot
    
    plot.plot_route_with_labels(route, coordinates)
    plot.plot_route_with_labels(new_route, coordinates)
    

