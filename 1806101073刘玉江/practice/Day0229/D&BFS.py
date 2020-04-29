graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def BFS(graph, start):
    queue = []  # 用数组表示队列
    queue.append(start)
    seen = set()  # 存放已经见过的结点，集合
    seen.add(start)
    while (len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)

def DFS(graph,start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    while(len(queue)>0):
        vertex = queue.pop()
        node = graph[vertex]
        for w in node:
            if w not in seen:
                seen.add(w)
                queue.append(w)
        print(vertex)




DFS(graph,"A")
#BFS(graph, "A")
