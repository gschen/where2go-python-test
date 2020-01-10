import os
#os.system("ipconfig")#不返回结果

d = os.popen("ipconfig")
print(d.read())#返回结果