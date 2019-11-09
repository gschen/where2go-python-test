"""
模拟交通警察的雷达测速仪。输入汽车速度，如果速度超出60 mph，则显示“Speeding”，否则显示“OK”。
在一行中输出测速仪显示结果，格式为：Speed: V - S，其中V是车速，S或者是Speeding、或者是OK。
"""
spe = int(input())
if spe <= 60:
    print("Speed:",spe,"-","OK")
else:
    print("Speed:",spe,"-","Speeding")