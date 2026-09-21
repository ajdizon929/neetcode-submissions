class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.length = 0
    
    def get(self, index: int) -> int:
        if index in range(0,self.length):
            cur = self.head.next
            for i in range(index):
                cur = cur.next
            return cur.getVal()
        else:
            return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.head.next)
        self.head.next = new_node
        # if empty list, tail is still head
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def remove(self, index: int) -> bool:
        if index in range(0,self.length):
            cur = self.head
            for i in range(index):
                cur = cur.next
            to_remove = cur.next
            cur.next = to_remove.next
            # update tail if removed tail
            if to_remove == self.tail:
                self.tail = cur
            self.length -= 1
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        values = []
        cur_node = self.head.next
        while cur_node:
            values.append(cur_node.getVal())
            cur_node = cur_node.next
        return values

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getVal(self) -> int:
        return self.val