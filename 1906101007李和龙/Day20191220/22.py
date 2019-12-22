class A(object):
    def __init__(self):
        print("A")
        super(A,self).__init__()
class B(object):
    def __init__(self):
        print("B")
        super(B,self).__init__()
class C(A):
    def __init__(self):
        print("C")
        super(C,self).__init__()
class D(A):
    def __init__(self):
        print("D")
        super(D,self).__init__()
class E(B,C):
    def __init__(self):
        print("E")
        super(E,self).__init__()
class F(C,B,D):
    def __init__(self):
        print("F")
        super(F,self).__init__()
class G(D,B):
    def __init__(self):
        print("G")
        super(G,self).__init__()
if __name__ == "__main__":
   # g = G()
    f = F()

