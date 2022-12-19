def insertion_sort():
  
  numbers = input("Enter a list of numbers, separated by spaces: ").split()
  numbers = [int(x) for x in numbers]

  
  for i in range(1, len(numbers)):
    current_value = numbers[i]
    hole = i
    while hole > 0 and numbers[hole - 1] > current_value:
      numbers[hole] = numbers[hole - 1]
      hole -= 1
    numbers[hole] = current_value
  return numbers

sorted_numbers = insertion_sort()
print(sorted_numbers)
