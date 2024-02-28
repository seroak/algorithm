import sys
n = int(input())
arr = list(map(int, input().split()))
left = 0
right = len(arr) - 1
arr.sort()
num1 = 0
num2 = 0
mn = sys.maxsize
while left < right:
    result = arr[left] + arr[right]
    if result == 0:
        num1 = arr[left]
        num2 = arr[right]
        break
    elif result < 0:
        if abs(result) < mn:
            num1 = arr[left]
            num2 = arr[right]
            mn = abs(result)
        left += 1
    else:
        if abs(result) < mn:
            num1 = arr[left]
            num2 = arr[right]
            mn = abs(result)
        right -= 1
print(num1, num2)