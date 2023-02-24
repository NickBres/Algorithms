class Vertex:  # graph node
    def __init__(self):
        self.color = 'white'  # white - not discovered, gray - not finished, black - finished
        self.d = float('inf')  # distance from start to self
        self.pi = None  # number of father
        self.f = float('inf') # finishing time (when became black)
        self.neighbours = []  # list of numbers of neighbours

def BFS(graph,start): # O(|edges| + |nodes|)
    graph[start].color = 'gray'
    graph[start].d = 0
    queue = [start]  # nodes to check
    while len(queue):  # run on nodes in queue
        u = queue.pop()
        for vertex_num in graph[u].neighbours:  # run on node's neighbours
            if graph[vertex_num].color == 'white':  # neighbour not discovered
                graph[vertex_num].color = 'gray'
                graph[vertex_num].d = graph[u].d + 1
                graph[vertex_num].pi = u
                queue.append(vertex_num)
        graph[u].color = 'black'


def DFS(graph): # O(|edges| + |nodes|)
    time = 0
    for vertex in graph:
        if vertex.color == 'white':
            DFS_visit(graph,vertex,time)

def DFS_visit(graph,vertex,time):
    time +=1
    vertex.color = 'gray'
    vertex.d = time
    for vertex_num in vertex.neighbours:
        if graph[vertex_num].color == 'white':
            graph[vertex_num].pi = vertex
            time = DFS_visit(graph,graph[vertex_num],time)
    vertex.color = 'black'
    time += 1
    vertex.f = time
    return time




