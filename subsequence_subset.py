'''
LOGIC-
Take the 0th element
pass the remaining array elements as they are still left to process.
Then the 2 recursive calls for both scenarios-
1) Take- Add the element you are making decision for (0th element) to the currentAns array
func(currentAns+[ele] , remainingArray , totalResult)
2- Not take- Skip the element you are making decision for (0th element) to the ans array
func(currentAns , remainingArray , totalResult)
'''

# Leetcode solution

class Solution(object):
    def subsetsFunc(self,nums,ans,finalResult):
        if len(nums)==0:
            finalResult.append(ans)
            return
        
        ele=nums[0]
        remainingArray=nums[1:]

        self.subsetsFunc(remainingArray,ans+[ele],finalResult)
        self.subsetsFunc(remainingArray,ans,finalResult)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        finalResult=[]
        self.subsetsFunc(nums,[],finalResult)
        return finalResult
