class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_linked_lists(headX, headY):
    """
    Merge two sorted linked lists into one sorted linked list.

    Parameters:
    headX (ListNode): The head of the first sorted linked list.
    headY (ListNode): The head of the second sorted linked list.

    Returns:
    ListNode: The head of the merged sorted linked list.
    """
    dummy = ListNode()
    tail = dummy

    while headX and headY:
        if headX.value < headY.value:
            tail.next = headX
            headX = headX.next
        else:
            tail.next = headY
            headY = headY.next
        tail = tail.next

    tail.next = headX or headY

    return dummy.next

def print_linked_list(head):
    """
    Print the elements of a linked list.
    """
    while head:
        print(head.value)
        head = head.next

def create_linked_list(values):
    """
    Create a linked list from a list of values.
    """
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# User input handling
if __name__ == "__main__":
    countX = int(input("Enter the number of elements in the first linked list: "))
    valuesX = [int(input()) for _ in range(countX)]
    countY = int(input("Enter the number of elements in the second linked list: "))
    valuesY = [int(input()) for _ in range(countY)]

    headX = create_linked_list(valuesX)
    headY = create_linked_list(valuesY)

    merged_head = merge_sorted_linked_lists(headX, headY)
    print("Merged linked list:")
    print_linked_list(merged_head)

