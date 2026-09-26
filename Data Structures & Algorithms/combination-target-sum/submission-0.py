class Solution:

  def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i, current_combination, total):
      # Base case: if we hit the target, add a copy of the combination
      if total == target:
        res.append(list(current_combination))
        return
      # Base case: if we exceed the target or go out of bounds
      if total > target or i >= len(nums):
        return

      # Choice 1: Include the current element (can be reused, so index remains 'i')
      current_combination.append(nums[i])
      dfs(i, current_combination, total + nums[i])
      current_combination.pop()  # Backtrack

      # Choice 2: Exclude the current element and move to the next index 'i + 1'
      dfs(i + 1, current_combination, total)

    dfs(0, [], 0)
    return res