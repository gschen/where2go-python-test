class Node(object):
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

    def __str__(self):
        return self.w

def up(node):
    return Node(node.x - 1, node.y, node.w+"U")

def down(node):
    return Node(node.x + 1, node.y, node.w+"D")

def left(node):
    return Node(node.x, node.y - 1, node.w+"L")

def right(node):
    return Node(node.x, node.y + 1, node.w+"R")

if __name__ == '__main__':
    m, n = map(int, input().split())
    visited = set()
    queue = []
    map_int = [[0] * (n + 1)]
    for i in range(1, m+1):
        map_int.append([0]*(n+1))
        nums = input()
        nums = "0" + nums
        for j in range(0, n+1):
            map_int[i][j] = ord(nums[j]) - 48

    node = Node(1, 1, "")
    queue.append(node)
    while len(queue) != 0:
        moveNode = queue[0]
        queue.pop(0)
        moveStr = str(moveNode.x) + " "+ str(moveNode.y)
        if moveStr not in visited:
            visited.add(moveStr)
            if moveNode.x == m and moveNode.y == n:
                print(len(moveNode.__str__()))
                print(moveNode)
                break
            if moveNode.x < m:
                if map_int[moveNode.x + 1][moveNode.y] == 0:
                    queue.append(down(moveNode))
            if moveNode.y > 1:
                if map_int[moveNode.x][moveNode.y - 1] == 0:
                    queue.append(left(moveNode))
            if moveNode.y < n:
                if map_int[moveNode.x][moveNode.y + 1] == 0:
                    queue.append(right(moveNode))
            if moveNode.x > 1:
                if map_int[moveNode.x - 1][moveNode.y] == 0:
                    queue.append(up(moveNode))

