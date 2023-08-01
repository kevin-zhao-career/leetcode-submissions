object Solution {
    def check(nums: Array[Int], target : Int, current: Int, cursor: Int): Array[Int] = {
        if (current > nums.length) Array.emptyIntArray
        else if (current != cursor && nums(current) + nums(cursor) == target) Array(current,cursor)      
        else if (cursor < nums.length - 1) check(nums, target, current, cursor + 1)      
        else check(nums, target, current + 1, 1)
    }
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        check(nums, target, 0, 1)
    }
}
