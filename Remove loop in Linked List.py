class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # Step 1: Pehle loop detect karo using Floyd's Cycle Detection Algorithm
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # Agar slow aur fast milte hain, toh loop hai
            if slow == fast:
                break
        else:
            # Agar loop nahi mila, toh return karo — koi change nahi karna
            return

        # Step 2: Loop mil gaya, ab loop ka start node dhoondo
        slow = head
        if slow == fast:
            # Jab loop head se start ho raha ho
            while fast.next != slow:
                fast = fast.next
        else:
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

        # Step 3: Loop tod do — by pointing last node's next to None
        fast.next = None
