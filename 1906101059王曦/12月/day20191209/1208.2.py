# 有 n 位用户参加活动，他们的 ID 从 0 到 n - 1，每位用户都 恰好 属于某一用户组。
# 给你一个长度为 n 的数组 groupSizes，其中包含每位用户所处的用户组的大小，
# 请你返回用户分组情况（存在的用户组以及每个组中用户的 ID）
class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        ll = []
        for i in range(len(groupSizes)):
            if groupSizes[i] != 0:
                lis =[i]
            if groupSizes[i] == 1:
                ll.append(lis)
                groupSizes[i] = 0
            for j in range(i+1,len(groupSizes)):
                if groupSizes[i]>len(lis) and groupSizes[i] == groupSizes[j]:
                    lis.append(j)
                    groupSizes[j] = 0
                    if groupSizes[i] == len(lis):
                        ll.sort()
                        if lis not in ll:
                            ll.append(lis)
        return ll