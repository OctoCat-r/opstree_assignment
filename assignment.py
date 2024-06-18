
# Aman Jain(E21CSEU0853)
# Problem Statement: Arithmetic Operations via Linked List
# WAP that via which we can perform arithmetic operations. The program should support below operations
# Take numbers as input
# Program should store number as LinkedList
# Print number as LinkedList traversal
# Can perform below operations
# Addition
# Subtraction
# Multiplication

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        
    # adding input in linked list
    def add_in_list(self, num):
        if self.head is None:
            self.head = ListNode(num)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(num)
    def print_List(self):
        current = self.head
        while current:
            print(current.val, end=' ')
            current = current.next
        print()
    
    def add_all(self):
        # temp = ListNode(0)
        # a,b,current = l1.head, l2.head, temp
        
        # carry = 0;
        # while a is not None or b is not None:
        #     x = a.val if a is not None else 0
        #     y = b.val if b is not None else 0
            
        #     total = carry + x + y
        #     carry = total // 10
            
        #     current.next = ListNode(total % 10)
        #     current = current.next
        #     if a is not None: a = a.next
        #     if b is not None: b = b.next
            
        #     if carry>0:
        #         current.next = ListNode(carry)
        #     result = LinkedList()
        #     result.head = temp.next
        #     return result
        
        if self.head is None:
            return 0
        total = 0;
        current = self.head
        while current:
            total +=current.val
            current = current.next
        return total
            
    def sub_all(self):
        if self.head is None:
            return 0
        # total = 0;
        current = self.head
        total = current.val
        current = current.next
        while current:
            total -=current.val
            current = current.next
        return total
        
    def multiply_all(self):
        if self.head is None:
            return 0
        total = 1;
        current = self.head
        while current:
            total *=current.val
            current = current.next
        return total
        
        
def create_linkedList():
    ll = LinkedList()
    n = int(input("Enter the number of element you want "))
    for _ in range(n):
        num = int(input("Enter a number: "))
        ll.add_in_list(num)
    return ll
list1 = create_linkedList()
list1.print_List()

list_sum = list1.add_all()
list_sub = list1.sub_all()
list_mul = list1.multiply_all()

print("sum: ", list_sum)
print("sub: ", list_sub)
print("mul: ", list_mul)

    
            
