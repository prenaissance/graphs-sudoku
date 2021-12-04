from classes import Node
def main():
    testnode=Node(1)
    testnode2=Node(2)
    testnode3=Node(3)
    testnode.addEdge(testnode2)
    testnode.addEdge(testnode3)
    print(testnode2)
if __name__=="__main__":
    main()
