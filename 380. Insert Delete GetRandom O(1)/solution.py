class RandomizedSet:

    """
    The insert and remove operation could simply be implemented using a HashSet, but for getRandom function
    we need a way to pick a random index and HashMap is not useful here. We can use a list instead.
    """

    def __init__(self):
        self.hashmap = {}
        self.list = []


    def insert(self, val: int) -> bool:
        #check if the value is in the set
        res = val not in self.hashmap
        if res:
            #add val both in HashMap and list
            self.hashmap[val] = len(self.list)
            self.list.append(val)

        return res


    def remove(self, val) -> bool:

        res = val in self.hashmap

        if res:
            #Swap the element that we want to remove with the last one and pop it
            #This way we delete the element without moving all the elements from the right which is O(n)
            index = self.hashmap[val]
            lastVal = self.list[-1]
            self.list[index] = lastVal
            self.list.pop()
            self.hashmap[lastVal] = index
            del self.hashmap[val]

        return res

    def getRandom(self) -> int:
        #we just pick a random element from the list
        import RandomizedSet
        return random.choice(self.list)