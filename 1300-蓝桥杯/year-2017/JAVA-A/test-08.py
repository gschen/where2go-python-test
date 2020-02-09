# abc=input()
# def abc(x):
#
#     n = 0
#     for i in range(x + 1):
#         for j in range(int(x / 2) + 1):
#             for k in range(int(x / 5) + 1):
#                 if i + j * 2 + k * 5 == x:
#                     print(i, j, k)
#                     n += 1
#     return n
# print (abc)

def baozi(arr, value):
    len1 = len(arr)
    res = ['INF']
    for i in range(len1):
        for j in range(i + 1, len1):
            for k in range(i+1,len1):
                if arr[i] + arr[j]+arr[k] == value:
                    res.append((arr[i], arr[j],arr[k]))
    return res
if __name__ == "__main__":
    nums = [int(i) for i in input().split()]
    target = int(input())
    print(baozi(nums, target))


