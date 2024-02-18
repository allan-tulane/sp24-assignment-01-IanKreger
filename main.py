"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  if x<= 1:
    return x
  else:
    return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
  max = 0
  count = 0
  for item in mylist:
    if item == key:
      count += 1
      if count >= max:
        max = count
    else:
      count = 0
  return max
  


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
  if len(mylist) == 1:
    if mylist[0] == key:
      return Result(left_size=1, right_size=1, longest_size=1, is_entire_range=True)
    else:
      return Result(left_size=0, right_size=0, longest_size=0, is_entire_range=False)


  mid = len(mylist)//2
  left_half = mylist[:mid]
  right_half = mylist[mid:]

  left_result = longest_run_recursive(left_half, key)
  right_result = longest_run_recursive(right_half, key)

  if left_result.is_entire_range and right_result.is_entire_range:
    return Result(left_size=len(left_half) + right_result.left_size,
      right_size=len(right_half) + left_result.right_size,
      longest_size=len(left_half) + len(right_half),
      is_entire_range=True)
  elif left_result.is_entire_range:
    return Result(left_size=len(left_half) + right_result.left_size,
      right_size=right_result.right_size,
      longest_size=max(left_result.longest_size, right_result.longest_size),
      is_entire_range=False)

  elif right_result.is_entire_range:
    return Result(left_size=left_result.left_size,
      right_size=len(right_half) + left_result.right_size,
      longest_size=max(left_result.longest_size, right_result.longest_size),
      is_entire_range=False)
  else:
    return Result(left_size=left_result.left_size,
      right_size=right_result.right_size,
      longest_size=max(left_result.longest_size, right_result.longest_size, left_result.right_size + right_result.left_size),
      is_entire_range=False)
    

