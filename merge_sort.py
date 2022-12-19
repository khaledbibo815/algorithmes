def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    # Split the list in half
    middle = len(numbers) // 2
    left = numbers[:middle]
    right = numbers[middle:]
    
    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    # Add any remaining elements
    result.extend(left)
    result.extend(right)
    return result

# Prompt the user to enter a list of numbers
print("Enter a list of numbers, separated by spaces:")
numbers_string = input()

# Convert the string into a list of numbers
numbers = [int(x) for x in numbers_string.split()]

# Sort the numbers using merge sort
sorted_numbers = merge_sort(numbers)

# Print the sorted list
print(sorted_numbers)
