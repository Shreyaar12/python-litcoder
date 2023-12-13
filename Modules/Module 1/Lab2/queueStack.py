# Queue
# Write a program to implement a custom queue using two stacks. The queue should support the following three types of queries:
# Enqueue: This query type is denoted by "1 x", where x is an element to be enqueued. It means that you need to insert element x at the end of the queue.
# Dequeue: This query type is denoted by "2". It indicates that you should remove the element at the front of the queue.
# Print Front: This query type is denoted by "3". It instructs you to print the element at the front of the queue without removing it.

# Exercise-1
# input:
# 1 42,2,1 14,3

# output:
# 14

# Exercise-2
# input:
# 1 23,2,1 14,3,2,1 78,3

# Output:
# 14
# 78

class CustomQueue:
    def __init__(self):
        self.stack1 = []  # For enqueue operation
        self.stack2 = []  # For dequeue operation

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                return None  # The queue is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def print_front(self):
        if not self.stack2:
            if not self.stack1:
                return None  # The queue is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        front_element = self.stack2[-1]
        return front_element

# Function to perform operations based on input
def doSomething(input_val):
    queue = CustomQueue()
    output = []

    queries = input_val.split(',')
    for query in queries:
        operation, *args = query.split()
        if operation == '1':
            element = int(args[0])
            queue.enqueue(element)
        elif operation == '2':
            queue.dequeue()
        elif operation == '3':
            front_element = queue.print_front()
            if front_element is not None:
                output.append(front_element)

    return output

# Example input for Exercise-1
input_val_1 = "1 42,2,1 14,3"
output_val_1 = doSomething(input_val_1)
for i in output_val_1:
    print(i)  # Output: [14]

# Example input for Exercise-2
input_val_2 = "1 23,2,1 14,3,2,1 78,3"
output_val_2 = doSomething(input_val_2)
for i in output_val_2:
    print(i) 
