# TLE working recursive code
# Recursive code is not possible for this problem because TLE and RuntimeError: maximum recursion depth exceeded error will come

'''Recursion LOGIC-
1-Fix the starting index i and try every possible ending index j from i + 1 onward.
2-For each subarray arr[i:j], calculate its sum using sum(arr[i:j]).
3-If the sum equals k, increment ans and pass it to the next recursive call.
4-Once all subarrays starting at i are checked, move to the next starting index using i + 1.
5-Continue until i == len(arr), then return the total count ans.'''

class Solution(object):
    def subarrays(self, arr, k, ans, i=0, j=1):
        if i == len(arr):
            return ans

        if j <= len(arr):
            if sum(arr[i:j]) == k:
                ans += 1

            return self.subarrays(arr, k, ans, i, j + 1)

        return self.subarrays(arr, k, ans, i + 1, i + 2)

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.subarrays(nums, k, 0)

      
# Correct complete solution does not include recursion it will be solved using hashmap technique
