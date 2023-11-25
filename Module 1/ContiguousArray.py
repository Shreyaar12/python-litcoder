import sys
def max_contiguous_subarray(nums):
    count = 0
    max_length = 0
    sum_indices = {0: -1}

    for i, num in enumerate(nums):
        if num == 0:
            count -= 1
        else:
            count += 1

        if count in sum_indices:
            max_length = max(max_length, i - sum_indices[count])
        else:
            sum_indices[count] = i

    return max_length

def doSomething(input_val):
    nums = list(map(int, input_val.split()))
    return max_contiguous_subarray(nums)

inputVal = input()
outputVal = doSomething(inputVal)
print(outputVal)
