# time - O(N*N)
# space - O(N)
class Solution:

  def numTrees(self, n: int) -> int:
    obj = {}

    obj[0] = 1
    obj[1] = 1

    for i in range(2, n + 1):
      for turn in range(0, i):
        if i not in obj:
          obj[i] = obj[turn] * obj[i - turn - 1]
        else:
          obj[i] += obj[turn] * obj[i - turn - 1]

    return obj[n]


my = Solution()
n = 5
ans = my.numTrees(n)
print("ans", ans)

# Runtime: 20 ms, faster than 98.32% of Python3 online submissions for Unique Binary Search Trees.
# Memory Usage: 14 MB, less than 10.71% of Python3 online submissions for Unique Binary Search Trees.