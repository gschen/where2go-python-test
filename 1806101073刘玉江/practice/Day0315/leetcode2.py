class CustomStack:

    def __init__(self, maxSize):
        self.stack=[]
        self.maxSize=maxSize


    def push(self, x):
        if len(self.stack)<self.maxSize:
            self.stack.append(x)


    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            return -1


    def increment(self, k, val):
        if len(self.stack)<k:
            for i in range(len(self.stack)):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val
