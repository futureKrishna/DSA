'''LOGIC- 
Points to Remember-

1-Choose every element one by one.
ch = nums[i]

2-Remove the chosen element from the list.
ros = nums[:i] + nums[i+1:]

3-Add the chosen element to the current answer.
ans + [ch]

4-Recurse on the remaining elements.
self.permutations(ros, ans + [ch], finalResult)

5-Base case: when no elements remain, the current ans is a complete permutation.
if len(nums) == 0:
    finalResult.append(ans)
    return
6-Each recursive level fills one position of the permutation.
7-For n distinct elements, the total number of permutations is : n!

Mental model:
Choose → Remove → Recurse → Complete
Most important: don't always choose nums[0].
Choose ch = nums[i]  -> Correct
'''

# Recursive code- working 100%

class Solution(object):
    def permutations(self,nums,ans,finalResult):
        if len(nums)==0:
            finalResult.append(ans)
            return

        for i in range(len(nums)):
            ch=nums[i]
            ros=nums[:i]+nums[i+1:]
            self.permutations(ros,ans+[ch],finalResult)
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        finalResult=[]
        self.permutations(nums,[],finalResult)
        return finalResult
