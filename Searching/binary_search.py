'''Binary Search '''
'''
배열 내부의 데이터가 정렬되어 있다면 빠르게 데이터를 찾을 수 있다는 장점이 있지만 데이터가 정렬되어 있지 않다면 사용할 수 없습니다. 
탐색 범위를 절반씩 좁혀가며 데이터를 탐색할 수 있다는 특징이 있습니다. 
시간 복잡도는 O(log N)입니다. 
'''
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end = mid - 1
        else:
            start = mid +1 
    return None 


# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력 받기 
n = 10
target = 12
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = binary_search(array, target, 0, n - 1)
if result == None:
    print(None)
else:
    print(result + 1)
    print(result+1)

