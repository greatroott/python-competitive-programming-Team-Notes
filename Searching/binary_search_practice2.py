n, m = list(map(int, input().split(' ')))
arr = list(map(int, input().split()))
arr = sorted(arr)
start = 0 
end = max(arr)

# 이진 탐색 수행 
def binary_search(arr, target, start,end):
    result = 0 
    while start <= end: 
        total = 0 
        mid = (start+end)//2
        for x in arr:
            if x> mid:
                total += x-mid 
        if total <m :
            end = mid -1 
        else: # 최대한 덜 잘랐을 때가 정답이므로 
            result = mid 
            start = mid + 1 
    return result 

result = binary_search(arr, m, start,end)

print(result) 