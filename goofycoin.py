import SinglyLinkedList as ll
import NodeofList as node
import listvar as glob

class goofy_coin:

    def __init__(self):
        glob.goofy_list = ll.SinglyLinkedList()
        start_amount = input("Enter the amount to start the chain : ")
        genesis = node.ListNode(start_amount)
        genesis.me = "##GOOFY##"
        glob.goofy_list.add_node(genesis)

    def makecoin(self, value):
        temp_block = node.ListNode(value)
        temp_block.me = "##GOOFY##"
        temp_block.value = value
        glob.goofy_list.add_node(temp_block)

    def transaction(self, from_person, to_person, value):
        #### NODE OF GIVING TO OTHER ####
        temp_block = node.ListNode(value)
        temp_block.me = to_person
        temp_block.value = value
        #### NODE OF GIVING TO MYSELF ####
        temp_block2 = node.ListNode(value)
        temp_block2.me = from_person

        #glob.goofy_list.add_node(temp_block)
        currnode = glob.goofy_list.head
        flag = 0
        while currnode is not None:
            if currnode.me == from_person:
                if currnode.value >= value and currnode.spent == False:
                    flag = 1
                    temp_block.parent = currnode
                    temp_block2.parent = currnode
                    currnode.given_to = to_person
                    if currnode.value != value:
                        temp_block2.value= currnode.value-value
                        glob.goofy_list.add_node(temp_block)
                        glob.goofy_list.add_node(temp_block2)
                    else:
                        glob.goofy_list.add_node(temp_block)
                    currnode.spent=True
                    break
            currnode=currnode.next

        if flag == 0:
            print "Transaction Failed"


    def print_goofy_list(self):
        glob.goofy_list.print_list()

    def search_goofy_list(self,value):
        return glob.goofy_list.search_list(value)


################################## TEST CODE ##################################
g=goofy_coin()
g.makecoin(23)
g.makecoin(2)
g.makecoin(3)
g.makecoin(212123)
g.transaction("##GOOFY##","Sunchit",24)
g.print_goofy_list()

print g.search_goofy_list(212123)
print "HERE"
###############################################################################