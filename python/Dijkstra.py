def createGraph(size):
    graph = {}
    print("If 2 node are not connected write 99999")
    for i in range(size):
        supgraph = {}
        for j in range(size):
            print("From ",i," to ",j,": ",end='')
            n = int(input())
            supgraph[j] = n
        graph[i] = supgraph

    return graph
def dijkstra(graph, start, stop):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
 
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
 
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
 
    currentNode = stop
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[stop] != infinity:
        print('Shortest distance is ' + str(shortest_distance[stop]))
        print('And the path is ' + str(path))
        
def main():
  size = int(input("How many Node:"))
  mygraph = createGraph(size)

  start = int(input("Choose start point:"))
  stop = int(input("Choose stop point:"))

  dijkstra(mygraph, start, stop)

if __name__ =='__main__':
 main()