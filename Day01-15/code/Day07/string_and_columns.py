from typing import List

str2 = 'abc123456abc123456'

print(str2[2::3])  # c246
print(str2[::2])  # ac246
print(str2[-1::-1])  # 654321cba
print(f'str2.find(\"a\"): {str2.find("a")}')
print(str2.center(20, '*'))

list1 = [1, 2, 3, 4]
list2: List[int] = [3, 4, 5, 6]

list1.extend(list2)
print(f"list 1 extended list 2: {list1}")
list2[3] = 76
# extend 使用的不是
print(f"list 2 modified: {list1}")
