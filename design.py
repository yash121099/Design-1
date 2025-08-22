// Time Complexity :
// Space Complexity :
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach
# TC: O(1)
# SC: O(1)

class MyHashSet:

    def __init__(self):
        self.bucket1 = 1000 #for primary hash
        self.bucket2 = 1000 #for secondary hash  
        self.storage = [None] * self.bucket1  #only primary bucket because it will take only 1000 space and will save another 1000 space
    
    def getPrimaryHash(self, key):
        return key % self.bucket1 # we will return which bucket that key will be there
    
    def getSecondaryHash(self, key):
        return key // self.bucket2 # will return about which spot inside that primary bucket

    def add(self, key: int) -> None:
        mainindex = self.getPrimaryHash(key) # to get bucket to find if there is secondary bucket is created or not 
        if self.storage[mainindex] is None: # To check if value from primary hash is none then we can create secondary bucket for that index
            if mainindex == 0: 
                self.storage[mainindex] = [False] * (self.bucket2 + 1) # for first postion there will be one more value in secondarybucket for the edge case that is last value 10^6
            else:
                self.storage[mainindex] = [False] *(self.bucket2) # others will get normal values 1000 secondary bucket size
        secondaryIndex = self.getSecondaryHash(key) # we will get value from the secondary hash where to add
        self.storage[mainindex][secondaryIndex] = True # will return true so that value is added
    def remove(self, key: int) -> None:
        mainindex = self.getPrimaryHash(key) # get index from the primary bucket
        if self.storage[mainindex] is None: # if there is no value at primary index then nothing to remove
            return
        secondaryindex = self.getSecondaryHash(key) #or there need to find secondary index value 
        self.storage[mainindex][secondaryindex] = False # make it false to remove from that secondary bucket of that primary index
    def contains(self, key: int) -> bool:
        mainindex = self.getPrimaryHash(key) # simalry findinf primary index to check if there is any value
        if self.storage[mainindex] is None:
            return False # if no value in that primary index return none
        secondaryIndex = self.getSecondaryHash(key) # else return secondary index
        return self.storage[mainindex][secondaryIndex] # return True or false according to the value present in that index


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)