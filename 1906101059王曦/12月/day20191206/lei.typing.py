from typing import List, Tuple, Dict

def add(a: int, string: str, f: float, b: bool) -> Tuple[List, Tuple, Dict, bool]:
    list1 = list(range(a))
    tup = (string, string, string)
    d = {"a": f}
    bl = b
    return list1, tup, d, bl
if __name__ == '__main__':
    print(add(5, 'mark', 183.1, False))
