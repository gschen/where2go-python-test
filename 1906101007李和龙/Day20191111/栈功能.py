"""
栈的功能
"""

class stack(object):
    def __init__(self):
        self.__list =  []


    def push(self,item):
        self.__list.append(item)

    def pop(self):
        self.__list.pop()

    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return self.__list == []
        # return not self.__list
    def size(self):
        return len(self.__list)
if __name__ == "__main__":
    s = stack()