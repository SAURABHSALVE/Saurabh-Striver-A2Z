class Solution(object):
    def getDecimalValue(self, head):
        temp = head 
        binary_str = ""
        
        # Step 1: Traverse and collect
        while temp:
            binary_str += str(temp.val) # Concatenate to string
            temp = temp.next            # Move to the next node!
            
        # Step 2: Convert to decimal
        # Python actually has a built-in way to convert binary strings to integers:
        return int(binary_str, 2)