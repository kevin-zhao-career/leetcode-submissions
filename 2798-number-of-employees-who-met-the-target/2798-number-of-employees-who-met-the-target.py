class Solution:
    def numberOfEmployeesWhoMetTarget(self, employeeHoursList: List[int], target: int) -> int:
        return len([employeeHours for employeeHours in employeeHoursList if employeeHours >= target])
