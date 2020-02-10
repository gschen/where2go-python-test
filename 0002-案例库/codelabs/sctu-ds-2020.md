# 数据结构课程实验
summary: 数据结构课程实验
id: sctu-ds-2020
categories: python
tags: sctu-ds 
status: Published 
authors: Chen Gongsuo
Feedback Link: http://www.sctu.edu.cn


## 环境配置
Duration: 20:00

利用QQ邮箱和真实姓名在https://github.com/网站注册账号；

在"我的电脑"的D盘创建文件夹dev，今后所有的课程相关软件、代码等资料都放置在该文件夹。


下载课程所需软件至D:\dev文件夹。


链接: https://pan.baidu.com/s/1AdbdK3Ygy5MgvFhGmtQoWQ 提取码: mvs4 
	

安装软件。
* git
* Anaconda 
* Pycharm


课程版本库：


https://github.com/sctu/sctu-ds-2019.git





Negative
: pycharm安装完成后，打开按照默认步骤进行，最后一步需要激活，激活方法请见：http://idea.lanyus.com/
	

Positive
: 请按照上述顺序安装软件，每个软件的安装都是next到底，一直Finish。请务必在实验课之前下载并完成安装上述软件。
	

不建议在安装的过程中，修改安装路径。如必须修改则需要牢记修改后的位置。
	







Anaconda安装




  





Pycharm安装






遇到问题
https://github.com/sctu/sctu-ds-2019/issues
打开网站，点击 New issue.


  







  

常见问题

## 实验一 链表的应用
Duration: 5:00

### 一、实验目的和要求 
1. 理解线性表的链式存储结构。 
1. 熟练掌握动态链表结构及有关算法的设计。 
1. 根据具体问题的需要，设计出合理的表示数据的链表结构，设计相关算法。

### 二、实验内容
1. 编程实现单链表的基本操作。
1. 使用前插法创建单链表；
1. 使用尾插法创建单链表；
1. 打印单链表中的每一个元素。
1. 第i个节点前插入新的节点。


```python
class Node:


    def __init__(self, value):
        self.value = value
        self.next = None




class List:


    def __init__(self):
        # 头节点
        self.head = Node(-1)


    # 前插法创建单链表
    def insert_before(self, data):
        for i in data:
            node = Node(i)


            if self.head.next is None:
                self.head.next = node
            else:
                node.next = self.head.next
                self.head.next = node


    # 尾插法创建单链表
    def insert_tail(self, data):


        tail = self.head.next


        for i in data:
            node = Node(i)


            if tail is None:
                self.head.next = node
                tail = node
            else:
                tail.next = node
                tail = node


    # 打印单链表
    def list_print(self):
        node = self.head.next


        while node:
            print(node.value)
            node = node.next


    # 清空链表
    def list_clear(self):
        self.head.next = None


    # 第i个节点前插入值为value的节点
    def list_element_add(self, i, value):


        node_new = Node(value)


        index = 0


        node = self.head.next


        while node:
            index = index + 1


            if index == i - 1:
                break


            node = node.next


        if node is None:
            return False


        node_new.next = node.next
        node.next = node_new




if __name__ == '__main__':
    my_list = List()


    my_list.insert_before([1, 2, 3, 4, 5])
    my_list.list_print()


    my_list.list_clear()


    my_list.insert_tail([1, 2, 3, 4, 5])
    my_list.list_print()


    my_list.list_element_add(3, 10)
    my_list.list_print()
```



	



2. 编程实现两个有序链表的合并。

```python
list_one = [1,3,5,7,9]
list_two = [2,4,6,8,10]


list_merged = [1,2,3,4,5,6,7,8,9,10]
```









## 实验二 栈和队列的应用
 Duration: 60:00


准备工作
栈的基本操作
新建python文件，命名为stack.py，输入下列内容开始练习。

```python
stack = []


# 压栈
stack.append(1)
stack.append(2)
stack.append(3)


# 出栈
print(stack.pop())  # 输出：3
print(stack.pop())  # 输出：2
print(stack.pop())  # 输出：1


for i in range(1, 10):
    stack.append(i)


# 当栈不为空时
while len(stack) is not 0:
    print(stack.pop())


	

队列的基本操作
新建python文件，命名queue.py，输入下列内容开始练习。
queue = []


# 入队
queue.append(1)
queue.append(2)
queue.append(3)


# 出队
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
```

	



1、编程实现字符串反转。
输入：Hello,World!
输出：!dlroW,olleH



```python

def reverse_str(input_str):
    stack = []
    target = []


    for ch in input_str:
        stack.append(ch)


    while len(stack) != 0:
        ch = stack.pop()
        target.append(ch)


    return target




if __name__ == '__main__':
    reverse_str('Hello,World!')

```
	



2、编程实现括号匹配。
输入：{[()]}
输出：True



```python

LEFT = ['(', '[', '{']
RIGHT = [')', ']', '}']




def parentheses_match(input_str):
    stack = []


    for ch in input_str:
        if ch in LEFT:
            stack.append(ch)
        elif ch in RIGHT:


            if len(stack) > 0 and RIGHT.index(ch) == LEFT.index(stack.pop()):
                continue
            else:
                return False


        else:
            print('The string contains not only parentheses!')
            return False


    if len(stack) == 0:
        return True


    return False




if __name__ == '__main__':
    print(parentheses_match('{[()]}'))
```

	



3、编程实现回文数判断。
输入：abcdcba
输出：True




```python
def is_palindrome(input_str):
    str_len = len(input_str)
    stack = input_str[:str_len / 2]


    if str_len % 2 == 0:
        queue = input_str[str_len / 2:]
    else:
        queue = input_str[str_len / 2 + 1:]


    while len(stack) != 0 and len(queue) != 0:
        if stack.pop() == queue.pop(0):
            continue
        return False


    if len(stack) == 0 and len(queue) == 0:
        return True


    return False




if __name__ == '__main__':
    # 需要将字符串转化为list，然后再进行处理，否则会出错
    print(is_palindrome(list('abcdcba')))

```
	



4、编程实现MinStack. 

```python

class MinStack:
    def __init__(self):
        self.data = []
        self.min_stack = []


    def get_min(self):
        return self.min_stack[len(self.min_stack) - 1]


    def push(self, num):
        self.data.append(num)


        if len(self.min_stack) == 0:
            self.min_stack.append(num)
        elif self.get_min() > num:
            self.min_stack.append(num)
        else:
            self.min_stack.append(self.get_min())


    def pop(self):
        if len(self.data) == 0:
            raise StackEmptyError('Stack Empty! No Element Pop!')


        self.min_stack.pop()
        return self.data.pop()


    def top(self):


        if len(self.data) > 0:
            return self.data[len(self.data) - 1]


        raise StackEmptyError('Stack Empty!')




class StackEmptyError(Exception):


    def __init__(self, value):
        self.value = value


    def __str__(self):
        return repr(self.value)




if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.get_min())


    min_stack.pop()
    print(min_stack.get_min())

```


	

## 实验三 树的应用
Duration: 30:00
一、实验目的和要求 
1. 理解二叉树的类型定义与性质。
2. 掌握二叉树的二叉链表存储结构的表示和实现方法。
3. 掌握二叉树遍历操作的算法实现。
4. 熟悉二叉树遍历操作的应用。
二、实验内容
1. 创建二叉树。
2. 先序、中序和后序遍历二叉树。
3. 按层次遍历二叉树。
4. 统计二叉树中节点个数。
5. 对二叉树中所有节点进行求和。


参考代码：


```python
class BiTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right




def count_BiTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BiTNodes(t.left) + count_BiTNodes(t.right)




def sum_BiTNodes(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BiTNodes(t.left) + sum_BiTNodes(t.right)




def preorder(t):
    if t is None:
        return
    print(t.data)
    preorder(t.left)
    preorder(t.right)




def inorder(t):
    if t is None:
        return
    inorder(t.left)
    print(t.data)
    inorder(t.right)




def postorder(t):
    if t is None:
        return
    postorder(t.left)
    postorder(t.right)
    print(t.data)








class BiTree:
    def __init__(self):
        self.root = None


    def add(self, data):
        if self.root is None:
            self.root = BiTNode(data)
        else:
            self.add_helper(self.root, data)


    def add_helper(self, node, data):
        if data <= node.data:
            if node.left is None:
                node.left = BiTNode(data)
            else:
                self.add_helper(node.left, data)
        elif data >= node.data:
            if node.right is None:
                node.right = BiTNode(data)
            else:
                self.add_helper(node.right, data)




if __name__ == '__main__':
    tree = BiTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)


    print(count_BiTNodes(tree.root))
    print(sum_BiTNodes(tree.root))


    inorder(tree.root)
    preorder(tree.root)
    postorder(tree.root)
```

	



## 实验四 图的应用
Duration: 30:00


### 一、实验目的和要求 
1.掌握图的存储思想及其存储。
2.掌握图的深度、广度优先遍历算法思想。
3.掌握图的常见应用算法的思想。

### 二、实验内容
1. 使用邻接表的方式存储图。

```python
a, b, c, d, e, f, g, h = range(8)
N = [
    {b, c, d, e, f},
    {c, e},
    {d},
    {e},
    {f},
    {c, g, h},
    {f, h},
    {f, g}
]
```

	

2. 使用邻接表的方式存储带权的图。

```python
a, b, c, d, e, f, g, h = range(8)
N = [


    {b:2, c:1, d:3, e:9, f:4},
    {c:4, e:4},
    {d:8},
    {e:7},
    {f:5},
    {c:2, g:2, h:2},
    {f:1, h:6},
    {f:9, g:8}
]
```

	

3. 使用邻接矩阵的方式存储图。

```python
a, b, c, d, e, f, g, h = range(8)


N =[
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]
```

	

4. 使用Dijkstra算法求解最短路径。

```python
# 图为邻接表形式
# Dijkstra算法
# 指定一个点到其他各顶点的路径——单源最短路径
# 初始化图参数
G = {1: {1: 0, 2: 1, 3: 12},
     2: {2: 0, 3: 9, 4: 3},
     3: {3: 0, 5: 5},
     4: {3: 4, 4: 0, 5: 13, 6: 15},
     5: {5: 0, 6: 4},
     6: {6: 0}}




def Dijkstra(G, v0, INF=999):
    """ 使用 Dijkstra 算法计算指定点 v0 到图 G 中任意点的最短路径的距离
        INF 为设定的无限远距离值
        此方法不能解决负权值边的图
    """
    book = set()
    minv = v0  # 源顶点到其余各顶点的初始路程
    dis = dict((k, INF) for k in G.keys())
    dis[v0] = 0


    while len(book) < len(G):
        book.add(minv)  # 确定当期顶点的距离
        for w in G[minv]:  # 以当前点的中心向外扩散
            if dis[minv] + G[minv][w] < dis[w]:  # 如果从当前点扩展到某一点的距离小与已知最短距离
                dis[w] = dis[minv] + G[minv][w]  # 对已知距离进行更新
        new = INF  # 从剩下的未确定点中选择最小距离点作为新的扩散点
        
        for v in dis.keys():
            if v in book:
                continue
            if dis[v] < new:
                new = dis[v]
                minv = v
    return dis




dis = Dijkstra(G, v0=1)
print(dis)
```