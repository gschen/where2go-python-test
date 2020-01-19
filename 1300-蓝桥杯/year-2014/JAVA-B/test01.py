'''
1.标题：武功秘籍
'''
star_page,end_page=map(int,input().split())
if star_page%2==0 and end_page%2!=0:
    result=(end_page-star_page+1)/2
else:
    result=((end_page-star_page+1)/2)+1
