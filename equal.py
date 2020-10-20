def equal_elements(l: list) -> bool:
      isequal = True
      i = 0;
      while True:
            if list[0] != list[i]:
                  isequal = False
            i = i + 1
      return isequal


print(equal_elements([1,2,3]))
print(equal_elements([2,2,2]))