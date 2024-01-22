'''
Initialization and CRUD for Array
'''
# Initialization
arr: list[int] = [0] * 5
value_arr: list[int] = [1, 2, 3, 4, 5]

# Accessing
def access(arr: list[int], index: int):
    assert index >= 0
    max_index = len(arr) - 1
    if index <= max_index:
        return arr[index]
    else:
        return ValueError(f"index should not greater than {max_index}")
    
# 增
def add(arr: list[int], value: int, index: int):
    max_index = len(arr) - 1
    assert index >= 0 and index <= max_index
    for i in range(max_index, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = value

# 删
def delete(arr: list[arr], index: int):
    max_index = len(arr) - 1
    assert index >= 0 and index <= max_index
    for i in range(index, max_index):
        arr[i] = arr[i + 1]


# 查
def search(arr: list[int], value: int):
    for index, val in enumerate(arr):
        if val == value:
            return index
    print("Not exists in current array")
    return -1
