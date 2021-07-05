class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
            
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_after_node(self,prev_node,data):
        if prev_node is None:
            print("previous node doesn't exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        
    def merge_list(self,llist):
        p = self.head
        q = llist.head
        s = None
        if not p :
            return q
        
        if not q :
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next =p
                s = p
                p = s.next
            else:
                s.next = q
                s= q
                q = s.next
        if not p :
            s.next = q
        if not q:
            s.next =p
        
        self.head = new_head
        return self.head
    
    def drop_duplicate(self):
        curr = self.head
        prev = None
        dup_value = dict()
        
        while curr:
            if curr.data in dup_value:
                # remove node
                prev.next = curr.next
                curr = None
            else:
                dup_value[curr.data] = 1
                prev = curr
            curr = prev.next
            
    def len_iterative(self):
        count = 0
        curr = self.head
        while curr:
            count+=1
            curr = curr.next
        return count
    
    def print_nth_from_last_node(self,n):
        total_len = self.len_iterative()
        curr = self.head
        while curr :
            if total_len==n:
                print("current data",curr.data)
                return curr.data
            else:
                total_len-=1
                curr = curr.next
        if curr is None:
            return
        
    def count_occurence_iterative(self,data):
        count =0 
        curr = self.head
        while curr:
            if curr.data == data:
                count+=1
                print("count",count)
            curr = curr.next
        return count
    
    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        
        sum_list = LinkedList()
        carry = 0
        while p or q:
            if not p :
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else :
                j = q.data
            s = i+j + carry
            if s>=10:
                carry =1
                remainder = s%10
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(s)
            if p:
                p= p.next
            if q:
                q = q.next
        return sum_list
                
                
    
            
# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# print("list before reversal")
# llist.print_list()
# llist.reverse_iterative()
# # llist.insert_after_node(llist.head,"D")
# print("list after reversal")
# llist.print_list()

# llist1 = LinkedList()
# llist2 = LinkedList()

# llist1.append("1")
# llist1.append("5")
# llist1.append("6")
# llist1.append("8")


# llist2.append("2")
# llist2.append("3")
# llist2.append("4")
# llist2.append("7")
# llist1.merge_list(llist2)


# llist3 = LinkedList()

# llist3.append("1")
# llist3.append("2")
# llist3.append("3")
# llist3.append("3")
# llist3.append("2")

# llist3.drop_duplicate()

# llist3.print_list()

# print(llist3.print_nth_from_last_node(2))
# print("*************$$$$$")
# print(llist3.count_occurence_iterative("3"))
# llist3.print_list()

llist1 = LinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

print(365 + 248)
llist1.sum_two_lists(llist2)
            
    
        