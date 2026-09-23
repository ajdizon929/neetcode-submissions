class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for string in strs:

            char_freq = [0] * 26
            if string:
                for char in string:
                    char_i = ord(char.lower()) - ord('a')
                    char_freq[char_i] += 1
            mapping = tuple(char_freq)
            anagram_dict[mapping] = anagram_dict.get(mapping, [])
            anagram_dict[mapping].append(string)
        return list(anagram_dict.values())