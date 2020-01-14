#用户分组
class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        _len = len(groupSizes)
        re = []
        if 0 != len:
            for i in range(_len):
                need = groupSizes[i]
                if 0 == need:
                    continue
                elif 1 == need:
                    re.append([i])
                else:
                    tmp = [i] * need
                    need -= 1
                    for j in range(i+1, _len):
                        if groupSizes[i] == groupSizes[j]:
                            groupSizes[j] = 0
                            tmp[need] = j
                            need -= 1
                            if not need > 0:
                                break
                    re.append(tmp)
        return re


