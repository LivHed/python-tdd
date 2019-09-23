def count_upper_case(message):
  #  count = 0
  #  for c in message:
  #     if c.isupper():
  #          count += 1
  #  return count
  
  return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("AA") == 2, "Two upper case"
assert count_upper_case("a") == 0, "one lower case"
assert count_upper_case("¤&?") == 0, "special characters"

print("All the tests passed")