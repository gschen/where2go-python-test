def check(prev_nums: list, number: int) -> bool:
    is_contained = (str(number) not in prev_nums)
    is_zero = ((10 * int(''.join(prev_nums)) + number) % len(prev_nums) == 0)
    return (is_contained and is_zero)
def search_num(prev_nums=['0']):
    for k in range(1, 10):
        if check(prev_nums, k):
            prev_nums.append(str(k))

            if len(prev_nums) - 1 == 9:
                return int(''.join(prev_nums))
            else:
                temp = search_num(prev_nums)
                if temp is not None:
                    return temp
    prev_nums.pop()
if __name__ == "__main__":
    print(search_num())