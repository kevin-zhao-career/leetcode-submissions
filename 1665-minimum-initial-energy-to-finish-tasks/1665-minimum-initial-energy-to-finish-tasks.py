# 1665. Minimum Initial Energy To Finish Tasks
# Author: Kevin Zhao
# Time Complexity: O(n log n)
# Space Complexity: O(1) if argument reuse, otherwise O(n)

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
