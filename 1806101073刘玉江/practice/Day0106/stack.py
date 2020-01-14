class Stack(object):
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit  # 设置容量

    def push(self, data):
        if len(self.stack) > self.limit:
            print('栈溢出')
            pass
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('空栈不能被弹出')

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size_stack(self):
        return len(self.stack)


stack = Stack(10)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

for i in range(stack.size_stack()):
    print('最顶层元素', stack.peek())
    print('是否为空：', stack.is_empty())
    print('size：', stack.size_stack())
    print(stack.pop())
