def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i, j =0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

arr = [6, 2, 8, 4, 1, 9, 3, 5, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)
