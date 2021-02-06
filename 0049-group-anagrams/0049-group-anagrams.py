from collections import defaultdict

def get_character_tuple_representation(string: str):
    character_count = [0] * 26
    for character in string:
        character_index = ord(character) - ord('a')
        character_count[character_index] += 1
    return tuple(character_count)

class Solution:
    def groupAnagrams(self, strings: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for string in strings:
            character_count_tuple = get_character_tuple_representation(string)
            anagrams[character_count_tuple].append(string)
        return anagrams.values()