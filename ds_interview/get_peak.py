arr = [3,5,2,4,1]

def get_peak(arr):
    start = 0
    end = len(arr)-1

    while True:
        mid = (start + end)//2
        left = arr[mid -1] if mid-1>=0 else float("-inf")
        right =  arr[mid+1] if mid+1 < len(arr) else float("-inf")
        if left < arr[mid] and right < arr[mid]:
            return mid
        elif arr[mid] < right:
            start = mid+1
        else:
            end = mid-1

print(get_peak(arr))