'''Sequential Search'''
# 시간복잡도는 O(N)입니다 
def sequential_search(n,target,array):
    idx = 1
    for i in array: 
        if i == target:
            return idx
        idx += 1 



print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split(" ")
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차 탐색 수행 결과 출력 
print(sequential_search(n,target,array))