class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

class List:
    def __init__(self):
        self.head=None

    def front(self):
        if self.head:
            return self.head.val
    
    def remove_front(self):
        if self.head:
            self.head=self.head.next
    
    def add_front(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node

#

class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

class List:
    def __init__(self):
        self.head=None

    def contains(self, val):
        runner=self.head
        while(runner):
            if runner.val == val:
                return True
            runner=runner.next
        return False

    def length(self):
        runner=self.head
        length=0
        while(runner):
            length+=1
            runner=runner.next
        return length
    
    def display(self):
        runner=self.head
        str=''
        while(runner):
            str+=f'{runner.val} -->'
            runner=runner.next
        return str