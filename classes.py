from typing import Any, List, Dict

#import matplotlib.pyplot as plt
#import networkx as nx


class Node():
    def __init__(self,num:int):
        self.num:int=num#the number of the sudoku tile
        self.edges:List=[]#edge list with other nodes
        self.edgeNums:List[int]=[]
    def __str__(self):#for testing
        s=f"Node {self.num}"
        s+="\nEdges:\n["
        for i in self.edges:
            s+=str(i.num)+" "
        s+="]"
        return s
    def addEdge(self,other):
        if self!=other:#no self loops
            if not(other in self.edges):
                self.edges.append(other)
                self.edgeNums.append(other.num)
                other.edges.append(self)
                other.edgeNums.append(self.num)
class Graph():
    def __init__(self,grid:List[List[int]]):
        #self.grid=grid#could be useful
        self.nodes:Dict[str,Node]={}#all nodes
        #Make all nodes:
        for i in range(9):
            for j in range(9):
                self.addNode(grid[i][j],i,j)
        #Connect nodes:
        for i in range(9):
            for j in range(9):
                for k in range(9):#column and row
                    self.addEdge(self.nodes[f"{i},{j}"],self.nodes[f"{i},{k}"])
                    self.addEdge(self.nodes[f"{i},{j}"],self.nodes[f"{k},{j}"])
                squarey=i-i%3
                squarex=j-j%3
                for y in range(squarey,squarey+3):
                    for x in range(squarex,squarex+3):
                        self.addEdge(self.nodes[f"{i},{j}"],self.nodes[f"{y},{x}"])
        #graph made from sudoku grid
    def addNode(self,num:int,i:int,j:int):
        self.nodes[f"{i},{j}"]=Node(num)
    def addEdge(self,a:Node,b:Node):
        a.addEdge(b)
    def isValid(self)->bool:
        for i in self.nodes.values():
            if i.num!=0:
                if i.num in i.edgeNums:
                    return False
        return True
    def visualize(self)->None:
        pass