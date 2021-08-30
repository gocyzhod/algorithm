이분탐색의 기본적인 개념 알고리즘

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None
result = binary_search(array, target, 0, n - 1)

전제조건 : 정렬되어 있어야 한다.
