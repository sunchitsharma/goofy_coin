class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.parent = None #
        self.me = None
        self.given_to = None #
        self.spent = False #
        self.signature = None
        return

    def has_value(self, value):
        if self.value == value:
            return True
        else:
            return False

    def is_payable(self, value):
        if self.value >= value:
            return True
        else:
            return False
