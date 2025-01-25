class Solution:
    """
    Time complexity:  O(n)
    Space complexity: O(n)
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        # create an array with the pair value of both position and speed
        pair = [[p, s] for p,s in zip(position, speed)]
        # we have to sort the array in reversed order as the last car will reach the target first
        for p, s in sorted(pair)[::-1]: 
            # calculate the time it get for the current car to reach the end
            time = (target - p) / s
            stack.append(time)

            if len(stack) > 1:
                # check if the current car reaches the target faster or in the same time
                # as the fleet ahead of it
                if stack[-1] <= stack[-2]:
                    # the car is added to the existing fleet
                    stack.pop()
        
        # each value from stack is a different fleet
        return len(stack)