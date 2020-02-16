def main(aim_str):
     i=0
     j=len(aim_str)-1
     result_number=0
     while i<=j:
         if aim_str[i]==aim_str[j]:
             i+=1
             j-=1
         else:
             #右指针
             right_index = j
             while aim_str[i]!=aim_str[right_index]:
                 right_index-=1

             #左指针
             left_index = i
             while aim_str[left_index] != aim_str[j]:
                 left_index += 1

             #指针移动距离
             right_distance=j-right_index
             left_distance=left_index-i

             if right_distance<left_distance:
                 result_number+=right_distance
                 j=right_index
             else:
                 result_number+=left_distance
                 i=left_index
     print(result_number)
main('ABCBA')
main('ABDCDCBABC')