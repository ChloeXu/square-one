class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def has_cycle(head):
  # TODO: Write your code here
  fast = head
  slow = head

  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
      return True
  return False


def find_cycle_length(head):
  # TODO: Write your code here
  fast = head
  slow = head
  l = 0
  slowFound = False

  # find the first meet-up of fast and slow, and use that as a base point
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
      slowFound = slow
      break
  # start with base point, traverse one step at a time to iterate thru 
  # until it's back at base point again
  current = slowFound
  while True:
    current = current.next
    l += 1
    if current == slowFound:
      return l

  return l

def find_cycle_start(head):
  cycle_length = find_cycle_length(head)
  print(cycle_length)
  fast = head
  for i in range(cycle_length):
    fast = fast.next
  slow = head
  while True:
    fast = fast.next
    slow = slow.next
    if fast == slow:
      break
  return fast

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  # print("LinkedList has cycle: " + str(has_cycle(head)))

  # head.next.next.next.next.next.next = head.next.next
  # print("LinkedList has cycle: " + str(has_cycle(head)))

  # head.next.next.next.next.next.next = head.next.next.next
  # print("LinkedList has cycle: " + str(has_cycle(head)))
 
  # head.next.next.next.next.next.next = head.next.next
  # print("LinkedList cycle length: " + str(find_cycle_length(head)))

  # head.next.next.next.next.next.next = head.next.next.next
  # print("LinkedList cycle length: " + str(find_cycle_length(head)))

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))  # ??????



main()