# Binary Search
- 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해서 앞에서부터 하나씩 데이터를 확인함
- 이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
    - 이진 탑색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.

## 이진 탐색의 시간 복잡도
- 단계마다 탐색 범위로 2로 나누는 것과 동일하므로 연산 횟수는 logN에 비례한다.
- 즉 이진 탐색은 범위를 절반씩 줄이며, 시간복잡도는 O(logN)을 보장한다.

## 구현

### 재귀적 구현 
```python
# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)
```
### 반복문 구현
```python
# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

## 파이썬 이진 탐색 라이브러리
```python
from bisect import bisect_left, bisect_right
```
위의 라이브러리를 이용하여 이진탐색을 구현할 수 있다.

## Parametric Search
- 조건을 만족하는 최소/최대값을 구하는 문제(최적화 문제)를 결정 문제로 변환해 이진 탐색을 수행하는 방법
    - 최적화 문제를 (yes or no)로 바꾸어 해결한다고 보면 된다.
    - 난이도가 높은 문제이기 때문에 스킵을 할 수도 있음.
