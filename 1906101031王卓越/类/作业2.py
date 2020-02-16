class Student(object):
    x=0
    def __init__(self):
        self.name='Bob'
        self.age=18
        self.sex='boy'
        self.english_mark=80
        self.chinese_mark=79
        self.math_mark=90
        Student.x+=1
    def mark(self):
        sum_mark= self.english_mark+ self.chinese_mark+  self.math_mark
        average_mark=(self.english_mark+ self.chinese_mark+  self.math_mark)/3
        return self.name,self.age,self.sex,self.english_mark,self.chinese_mark,self.math_mark, sum_mark,average_mark 
s=Student()
print(s.mark(),s.x)
k=Student()
print(s.mark(),s.x)
#王卓越
