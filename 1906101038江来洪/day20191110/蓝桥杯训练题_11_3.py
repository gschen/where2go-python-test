#用栈解决括号匹配问题
class Stack(object):
    def __init__(self):
        self.__list = []
    def push(self, item):
        self.__list.append(item)
    def pop(self):
        return self.__list.pop()
    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None
    def is_empty(self):
        return self.__list == []
    def size(self):
        return len(self.__list)
if __name__ == '__main__':
    s = Stack()
    str = input('请输入：')
    list1 = []
    list2 = ['(', '[', '{']
    list3 = [')', ']', '}']
    for i in str:
        if i in list2:
            s.push(i)
        elif i in list3:
            if i == ')':
                i = '('
                list1.append(i)
            elif i == ']':
                i = '['
                list1.append(i)
            elif i == '}':
                i = '{'
                list1.append(i)
    x = 0
    if s.size() == len(list1):
        if s.peek() == list1[0]:
            for n in list1:
                if n != s.pop():
                    x += 1
            if x == 0:
                print('True')
            else:
                print('False')
        else:
            for m in list1[::-1]:
                if m != s.pop():
                    x += 1
            if x == 0:
                print('True')
            else:
                print('False')
    else:
        print('False')