# Working code-
# Not optimized
  
class Solution(object):
  def subsetsFunc(self, nums, ans, target, finalResult):
      # Stop if the current sum has already exceeded target
      if sum(ans) > target:
          return

      if len(nums) == 0:
          if sum(ans) == target:
              finalResult.append(ans)
          return

      ele = nums[0]
      # remainingArrayIncludingCurrentElement = nums[0:]==nums
      remainingArray = nums[1:]

      self.subsetsFunc(nums,ans + [ele],target,finalResult)

      self.subsetsFunc(remainingArray,ans,target,finalResult)

  def combinationSum(self, candidates, target):
      """
      :type candidates: List[int]
      :type target: int
      :rtype: List[List[int]]
      """
      finalResult = []
      self.subsetsFunc(candidates, [], target, finalResult)
      return finalResult

    
  # Optmized code- minimal change, instead of making the whole subsequence and then doing sum of it and matching with target, 
  # we can directly pass currentSum in the recursive calls and match with target.

#we could have further optmized this by creating new arrays on every recursive call, we can use .append() and .pop() the element later


class Solution(object):
    def subsetsFunc(self, nums, currentSum, ans, target, finalResult):
        # Stop if the current sum has already exceeded target
        if currentSum > target:
            return

        if len(nums) == 0:
            if currentSum==target:
                finalResult.append(ans)
            return

        ele = nums[0]
        # remainingArrayIncludingCurrentElement = nums[0:]==nums
        remainingArray = nums[1:]
        self.subsetsFunc(nums,currentSum+ele,ans+[ele],target,finalResult)

        self.subsetsFunc(remainingArray,currentSum,ans,target,finalResult)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        finalResult = []
        self.subsetsFunc(candidates, 0, [], target, finalResult)
        return finalResult


# Slight optimization on the above code, using append() and pop() instead of creating new arrays everytime
class Solution(object):
    def subsetsFunc(self, nums, currentSum, ans, target, finalResult):
        # Stop if the current sum has already exceeded target
        if currentSum > target:
            return

        if len(nums) == 0:
            if currentSum==target:
                # because of updating ans using append() and pop() functions we are updating the ans array stored in finalResult, 
                # because python stores references so by doing ans[:] we are creating a new list with ans elements and then pushing.  
                finalResult.append(ans[:])
            return

        ele = nums[0]
        remainingArray = nums[1:]
        ans.append(ele)
        self.subsetsFunc(nums,currentSum+ele,ans,target,finalResult)
        ans.pop()
        self.subsetsFunc(remainingArray,currentSum,ans,target,finalResult)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        finalResult = []
        self.subsetsFunc(candidates, 0, [], target, finalResult)
        return finalResult

# MAX Optimized

class Solution(object):
    def backtrack(self, candidates, start, remaining, path, result):
        if remaining == 0:
            result.append(path[:])
            return

        for i in range(start, len(candidates)):
            ele = candidates[i]
            if ele > remaining:
                break
            path.append(ele)
            self.backtrack(candidates,i,remaining - ele,path,result)
            path.pop()

    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []
        self.backtrack(candidates,0,target,[],result)
        return result
