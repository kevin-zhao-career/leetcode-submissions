# 1665. Minimum Initial Energy To Finish Tasks
# Author: Kevin Zhao
# Time Complexity: O(n log n)
# Space Complexity: O(1) if argument reuse, otherwise O(n)
#
# Although, there is a sort involved, the trick to this solution is to ask the following:
# If for some k elements, the algorithm is true, what does the k+1th element do for our solution?
# Either the minimum energy we have to expend for the k+1th element is so large that the minimum effort for our k elements does
# not allow us to take that element, or it is enough, and we just have to expend the actual energy for the k+1th element.

def getActualEnergy(task : List[int]) -> int:
    return task[0]

def getMinimumEnergy(task : List[int]) -> int:
    return task[1]

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda task : getMinimumEnergy(task) - getActualEnergy(task))
        effort = 0
        for task in tasks:
            effort = max(effort + getActualEnergy(task), getMinimumEnergy(task))
        return effort
