def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum/ 2
  else:
      #(len(lst)/2) is converted to an integer to avoid indexing by a decimal
    return lst[int(len(lst) / 2)]

print(middle_element([5, -10, -4, 4, 5]))
