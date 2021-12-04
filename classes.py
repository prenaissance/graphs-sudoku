class Node():
    def __init__(self,num:int):
        self.num=num#the number of the sudoku tile
        self.edges=[]#edge list with other nodes
    def __str__(self):#for testing
        s=f"Node {self.num}"
        s+="\nEdges:\n["
        for i in self.edges:
            s+=str(i.num)+" "
        s+="]"
        return s
    def addEdge(self,other):
        if not(other in self.edges):
            self.edges.append(other)
            other.edges.append(self)