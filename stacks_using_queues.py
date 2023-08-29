"""
Leetcode 225: Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/

Implement a last-in-first-out (LIFO) stack using only two queues. The
implemented stack should support all the functions of a normal stack (push,
top, pop, and empty).

Implement the MyStack class:

  void push(int x) Pushes element x to the top of the stack.
  int pop() Removes the element on the top of the stack and returns it.
  int top() Returns the element on the top of the stack.
  boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

  You must use only standard operations of a queue, which means that only
	push to back, peek/pop from front, size and is empty operations are valid.

  Depending on your language, the queue may not be supported natively. You
	may simulate a queue using a list or deque (double-ended queue) as long as
	you use only a queue's standard operations.


Constraints:
  1 <= x <= 9
  At most 100 calls will be made to push, pop, top, and empty.
  All the calls to pop and top are valid.
"""


from collections import deque


class MyStack:
	def __init__(self):
		self.my_queue = deque()

	def push(self, x: int) -> None:
		self.my_queue.append(x)
		for i in range(len(self.my_queue) - 1):
			self.my_queue.append(self.my_queue.popleft())

	def pop(self) -> int:
		return self.my_queue.popleft()

	def top(self) -> int:
		return self.my_queue[0]

	def empty(self) -> bool:
		return (len(self.my_queue) == 0)

def stack_test(test_num):
	match test_num:
		case 0:
			obj = MyStack()
			obj.push("test")
			return obj.pop(), obj.empty()
		case 1:
			obj = MyStack()
			obj.push("test")
			return obj.top(), obj.empty()
		case 2:
			obj = MyStack()
			obj.push(1)
			obj.push(2)
			#return obj.top(), obj.pop(), obj.empty()
			param_1 = obj.top()
			param_2 = obj.pop()
			param_3 = obj.empty()
			return param_1, param_2, param_3

# Test cases
test_case_expected_strings = [("test", True), ("test", False), (2, 2, False)]

print()
print("Testing Report")
print("-" * 30)
num_passed = 0
for i in range(len(test_case_expected_strings)):
	output = stack_test(i)

	print("stack_test(" + str(i) + "):", output)

	test_case_expected_string = test_case_expected_strings[i]
	if (len(test_case_expected_string) > 20):
		test_case_expected_string = test_case_expected_string[:21] +\
																"... (" +\
																str(len(test_case_expected_string) - 20) +\
																" more chars)"
	print("\\" + "-" * (3 + len(str(i))) + "Expected:",
        test_case_expected_string)

	if (output == test_case_expected_strings[i]):
		print("Test case", i + 1, "passed!")
		num_passed += 1
	else:
		print("Test case", i + 1, "failed!")
	print()

print("Test cases passed:", str(num_passed / len(test_case_expected_strings) *
																100) + "%")
print("-" * 30)