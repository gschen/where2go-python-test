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
                #print(len(moveNode.__str__()))
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
'''
测试用例
30 50
01010101001011001001010110010110100100001000101010
00001000100000101010010000100000001001100110100101
01111011010010001000001101001011100011000000010000
01000000001010100011010000101000001010101011001011
00011111000000101000010010100010100000101100000000
11001000110101000010101100011010011010101011110111
00011011010101001001001010000001000101001110000000
10100000101000100110101010111110011000010000111010
00111000001010100001100010000001000101001100001001
11000110100001110010001001010101010101010001101000
00010000100100000101001010101110100010101010000101
11100100101001001000010000010101010100100100010100
00000010000000101011001111010001100000101010100011
10101010011100001000011000010110011110110100001000
10101010100001101010100101000010100000111011101001
10000000101100010000101100101101001011100000000100
10101001000000010100100001000100000100011110101001
00101001010101101001010100011010101101110000110101
11001010000100001100000010100101000001000111000010
00001000110000110101101000000100101001001000011101
10100101000101000000001110110010110101101010100001
00101000010000110101010000100010001001000100010101
10100001000110010001000010101001010101011111010010
00000100101000000110010100101001000001000000000010
11010000001001110111001001000011101001011011101000
00000110100010001000100000001000011101000000110011
10101000101000100010001111100010101001010000001000
10000010100101001010110000000100101010001011101000
00111100001000010000000110111000000001000000001011
10000001100111010111010001000110111010101101111000
'''
