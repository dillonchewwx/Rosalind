# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 20:17:10 2021
@author: dillonchewwx
Solution to tree on rosalind.info
"""

def main():
    with open("Data/rosalind_tree.txt") as file:
        lines = file.read().splitlines()
    num = int(lines[0])
    num_list = lines[1:]
    adj_list = []
    for i in range(len(num_list)):
       adj_list.append(set([int(x) for x in num_list[i].split()]))
    print(minEdges(num, adj_list))

def minEdges(num, adj_list):
    # Takes in a positive integer n and an adjacency list corresponding to a graph on n nodes that contains no cycle.
    # Returns the minimum number of edges that can be added to the graph to produce a tree. 
    
    # get cycles
    cycles = [set(adj_list[0])]
    for i, j in enumerate(adj_list):
        for k, l in enumerate(cycles):
            if j & l:
                cycles[k] = j|l
                break
        else:
            cycles.append(j)  

    # Number of connected nodes
    connected_nodes = sum(len(x) for x in cycles)
    
    # Number of isolated nodes
    isolated_nodes = num-connected_nodes
    
    # Minimum number of edges needed to connect n cycles is n-1
    # Minimum number of edges needed to connect n isolated nodes is n
    return len(cycles)-1+isolated_nodes
        
if __name__ == "__main__":
    main()


