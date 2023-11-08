def find_position(lists, target):
  def condition(mid):
    if lists[mid] == target:
      if mid > 0 and lists[mid - 1] == target:
        return 'left'
      else:
        return 'right'
    elif lists[mid] < target:
      return 'left'
    else:
      return 'right'

  return binary_search(0, len(lists)-1, condition)

def first_position(lists, target):
  def condition(mid):
    if lists[mid] == target:
      if mid > 0 and lists[mid-1] == target:
        return 'left'
      return 'found'
    elif lists[mid] < target:
      return 'right'
    else:
      return 'left'

  return binary_search(0, len(lists)-1, condition)

def last_position(lists, target):
  def condition(mid):
    if lists[mid] == target:
      if mid < len(lists)-1 and lists[mid+1] == target:
        return 'right'
      return 'found'
    elif lists[mid] > target:
      return 'left'
    else:
      return "right"

  return binary_search(0, len(lists)-1, condition)

  
def binary_search(low, high, condition):
  while low <= high:
    mid = (low + high) // 2
    result = condition(mid)
    if result == 'found':
      return mid
    elif result == 'left':
      high = mid - 1
    else:
      low = mid + 1
  return -1
