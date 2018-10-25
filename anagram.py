#navie soln

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p:
            return []
        
        anagram_idxs = []
        len_p = len(p)
        sorted_p = "".join(sorted(p))
        for idx, value in enumerate(s):
            if value in p and "".join(sorted(s[idx:idx+len_p])) == sorted_p:
                anagram_idxs.append(idx)
        
        return anagram_idxs
        

#working soln
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p:
            return []
        
        pvals = 26 * [0]
        for val in p:
            pvals[ord(val) - 97] += 1
        
        compare = 26 * [0]
        len_p = len(p)
        ans = []
        for idx, val in enumerate(s):
            compare[ord(val) - 97] += 1
            if idx >= len_p:
                compare[ord(s[idx - len_p]) - 97] -= 1
            if compare == pvals:
                ans.append(idx - len_p + 1)
        
        return ans

