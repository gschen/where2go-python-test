class classname(object):
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def student(self,data):
        if data<self.data:
            if self.left is None:
                self.left=data
            else:
                self.student(data)
        if data>self.data:
            if self.right is None:
                self.right=data
            else:
                self.right.student(data)
s=classname(10)
print(s.student(8))