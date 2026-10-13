class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        index_dict = {}

        while r < len(s):
            if s[r] in index_dict:
                max_len = max(max_len, r - l)
                for _ in range(l, index_dict[s[r]] + 1):
                    index_dict.pop(s[l])
                    l += 1
            index_dict[s[r]] = r
            r += 1
        return max(max_len, r - l)