def insertion_sort():
  # get a list of numbers from the user
  numbers = input("Enter a list of numbers, separated by spaces: ").split()
  numbers = [int(x) for x in numbers]

  # start at the second element of the list (the first one is already sorted)
  for i in range(1, len(numbers)):
    # store the current value to be sorted
    current_value = numbers[i]
    # start the "hole" at the current position
    hole = i
    # keep moving the hole to the left as long as the value at the hole is greater than the current value
    while hole > 0 and numbers[hole - 1] > current_value:
      # move the value at the hole to the right
      numbers[hole] = numbers[hole - 1]
      # move the hole to the left
      hole -= 1
    # put the current value into the hole
    numbers[hole] = current_value
  return numbers

sorted_numbers = insertion_sort()
print(sorted_numbers)
