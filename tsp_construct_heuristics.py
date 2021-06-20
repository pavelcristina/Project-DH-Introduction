# -*- coding: utf-8 -*-
"""
This file contains all functions related to the construction heuristic. 

@author: Pavel, Cristina-Maria, 11807972
       
"""

def calculation_lenght (Route,A): 
   cost = 0
   for i in range(len(Route)-1):
       cost += A[Route[i]][Route[i+1]]
       
   return(cost)


def make_dummy_route(matrix):
    
    solutions = []

    for startnode in range(len(matrix)):
        Route = [startnode]
    
        for i in range(len(matrix)):
       
            x= Route[-1]     # take the row of the last appended location in the route
            Msort = sorted (matrix[x]) # sort the selected row so you can find the nearest neighbour
            added = False
            for k in Msort: 
                if added == False:
                    for j in range(len(matrix)):
                        if matrix[x][j] == k and j not in Route: # can't just check for same value due to double value
                            Route.append(j)
                            added = True
    Route.append(Route[0])
    
    from tsp_construct_heuristics import calculation_lenght as lenght
    
    solutions.append((Route,lenght(Route,matrix),startnode))

    solutions.sort(key = lambda x: x[1])
    # print("The shortest Route starts at the Node ", solutions[0][2], "with the path" , solutions[0][0],"and the lenght " , solutions[0][1] )
    Route = solutions[0][0]
    startnode = solutions[0][2] 
    
    if startnode != 0:
        Route_zero = []
        for i in range(len(Route)): 
            if Route[i] == 0:
                break
            Route_zero =  Route[i+1:-1] +Route[0:i+1] + [0]
        
        else:
            Route_zero = Route
    
    return Route_zero

