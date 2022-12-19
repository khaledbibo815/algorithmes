def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    middle = len(numbers) // 2
    left = numbers[:middle]
    right = numbers[middle:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    result.extend(left)
    result.extend(right)
    return result

print("Enter a list of numbers, separated by spaces:")
numbers_string = input()

numbers = [int(x) for x in numbers_string.split()]

sorted_numbers = merge_sort(numbers)

print(sorted_numbers)
