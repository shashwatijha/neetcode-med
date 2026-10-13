class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l,r =0,0
        maxl, maxlen = 0,0;

        while r <= len(s)-1:
            if s[r] in seen:
                seen.remove(s[l])
                l+=1
            else:
                seen.add(s[r])
                r=r+1;
                maxl=max(maxl,r-l);
        return max(maxl,0);