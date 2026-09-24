#TLE Correct code
# This question cannot be solved using recursion as it will always give TLE or recursion depth is reached.

'''Recursion LOGIC-
1-Two indices define the subarray: i is the start and j is the end. This lets recursion systematically generate every possible subarray.
2-Use recursion to explore, not to store results: j expands the current subarray; once j reaches the end, move i forward and start a new set of subarrays.
3-Keep the current best answer as a parameter: minLen is passed through every recursive call, so each valid subarray can update the best minimum found so far.
4-Maintain state between recursive calls: currentSum carries the sum of the current subarray, avoiding recalculating sum(arr[i:j]) every time.
5-Always define a base case + "not found" state: when all starting positions have been explored, stop recursion. float('inf') represents "no valid subarray found"; convert it to 0 at the end.'''

class Solution(object):
    def subarrays(self,arr,target, minLen, i=0, j=1):
        if i == len(arr):
            return 0 if minLen == float('inf') else minLen

        if j <= len(arr):
            if sum(arr[i:j])>=target:
                minLen=min(minLen,j-i)
            return self.subarrays(arr,target, minLen, i, j + 1)
        else:
            return self.subarrays(arr,target, minLen, i + 1, i + 2)

    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        return self.subarrays(nums,target,float('inf'))
                    
