#二分法寻找一个数字在一个列表中的索引值


def binary_search(num_list,num):
    low = 0
    high = len(num_list)
    while low < high:

        mid = int((low+high)/2)
        guess_number = num_list[mid]
        if guess_number == num:
            return mid


        if guess_number > num:
            high = mid
        if guess_number < num:
            low = mid + 1

    return "该列表没有这个值"

print("__name__",__name__)


# print(binary_search([2,5,8,10,15,19,21],21))
if __name__ == "__main__":
    print(binary_search([2,5,8,10,15,19,21],21))
    print("End")
