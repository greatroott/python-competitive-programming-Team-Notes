'''실전 문제 2 (부품 찾기) -- 이진문제를 이용한 풀이 방법 난이도 1(Easy) '''
### 시간 제한 1초 
### 메모리 제한 128MB 
### input -> 최대 백만이기 떄문에, 시간 복잡도는 O(logN)이나 O(N) 이어야 함 
### 풀이 방법 -> binary search 
### 시간 복잡도 n *logN 방법으로 문제를 풀었다 
import sys 

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

n = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))
array = sorted(array)
# 손님이 입력한 부품의 개수 
m = int(sys.stdin.readline().strip())
m_array = list(map(int, sys.stdin.readline().strip().split()))
for i in range(m):
    res = binary_search(array,m_array[i],0,n-1)
    if res is None:
        print('no',end =" ")
    else:
        print("yes",end =" ")