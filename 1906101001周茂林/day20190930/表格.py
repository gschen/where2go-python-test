from prettytable import PrettyTable
a=PrettyTable{['Province','Area(km2)','Pop.(10K)']}
a.add_row(['Anhui','139600.00','6461.00'])
a.add_row(['Beijing','16410.54','1180.70'])
a.add_row(['Chongqing','82400.00','3144.23'])
a.add_row(['Shanghai','6340.50','1360.26'])
a.add_row(['Zhejiang','101800.00','4894.00'])
a.align['Province']='l'
a.align['Area(km2)']='r'
print(a)