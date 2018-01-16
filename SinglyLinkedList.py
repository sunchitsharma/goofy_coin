import NodeofList as node

class SinglyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
        return

    def add_node(self, item):
        if not isinstance(item,node.ListNode):
            item = node.ListNode(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next=item
        self.tail=item
        return

    def list_len(self):
        count =0;
        currnode = self.head
        while currnode is not None:
            count =count + 1
            currnode=currnode.next
        return count

    def print_list(self):
        currnode = self.head
        while currnode is not None:
            print (currnode.value)
            currnode=currnode.next
        return

node1 =node.ListNode(15)
node2 =node.ListNode("china")
item3 = 23

alist= SinglyLinkedList()
print("List Length : %i" % alist.list_len())

for curr_item in [node1, node2, item3]:
    alist.add_node(curr_item)
    print("List Length : %i" % alist.list_len())
    alist.print_list()
