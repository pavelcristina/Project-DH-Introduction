# -*- coding: utf-8 -*-
"""
This file contains all functions related to the local search heuristic. 

@author: Pavel, Cristina-Maria, 11807972
        
"""

import utils
import random as r




def make_dummy_ls(route, matrix):
    # make a copy of the route
    
    repeat = True
    zähler = 0 
    while repeat == True:
        copy_route = list(route)
        
      
        segment_length = r.randint(1,3)
    
        start_index = r.randint(1, len(copy_route)-1-segment_length)
        segment_array = copy_route[start_index:start_index+segment_length]
        array_without_segment = copy_route[0:start_index] +copy_route[start_index+segment_length:]
    
        # print(segment_array)
        # print(array_without_segment)
    
        for i in range(len(array_without_segment)-1):
            zähler += 1
            array = array_without_segment
            segment = segment_array
            combination_array = array[:i+1] + segment + array[i+1:]
            # print(combination_array, "with len:" , len(combination_array))
          # calculate its cost
            cost = utils.calc_cost(copy_route, matrix)
            new_cost = utils.calc_cost(combination_array, matrix)
            if new_cost < cost:
                cost = new_cost
                repeat = False 
                break
        if repeat == False or zähler == 100000:
            break
        
        
        
    return(combination_array, cost)


    







