# TLE working code

class Solution:
    def subsetsFunc(self,nums,target,ans):
        if len(nums)==0:
            if sum(ans) == target:
                return 1
            return 0


        ele=nums[0]
        remainingArray=nums[1:]

        take=self.subsetsFunc(remainingArray,target,ans+[ele])
        notTake=self.subsetsFunc(remainingArray,target,ans)
        
        return take+notTake
	def perfectSum(self, arr, target):
		# code here
		return self.subsetsFunc(arr,target,[])


'''if we want to maintain a result varible which will store the count of subsets equal target, then we will not take answers from the recursive calls seperately and then add them later.
We can simply get the result of both the recursive calls in the same ans variable and then return this and variable at the end.

So instead of returning 1 or 0 for each subset and then adding the results received from both the recursive calls, we can simply add +1 to our answer in the base case for correct subset
(Code below for this ie. maintaining a ans variable and passing it to the next recursive calls )'''

def subsetsFunc(self, nums, current, target, ans):
    if len(nums) == 0:
        if sum(current) == target:
            ans += 1
        return ans

    ele = nums[0]
    remainingArray = nums[1:]

    ans = self.subsetsFunc(
        remainingArray, current + [ele], target, ans
    )

    ans = self.subsetsFunc(
        remainingArray, current, target, ans
    )

    return ans
