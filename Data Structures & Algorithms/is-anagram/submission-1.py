class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}

        if len(s) != len(t):
            return False

        for c in s:
            if c not in char_map:
                char_map[c] = 1
            else:
                char_map[c] += 1

        for c in t:
            if c not in char_map or char_map[c] == 0:
                return False
            char_map[c] -= 1
            
        return True
        