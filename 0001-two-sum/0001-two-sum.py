class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        number_to_index_hash_map = {}
        for index, number in enumerate(numbers):
            complement = target - number
            if complement not in number_to_index_hash_map:
                number_to_index_hash_map[number] = index
            else:
                return [number_to_index_hash_map[complement], index]