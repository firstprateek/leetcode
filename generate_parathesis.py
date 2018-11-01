class Solution:
  def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    if not n or (n < 2):
        return []

    res = []

    counts = { '(': n, ')': n}

    def util(comb = []):
        if len(comb) == 2*n:
            res.append("".join(comb))
        
        for paran, count in counts.items():
            if count == 0: continue
            
            comb.append(paran)
            counts[paran] -= 1
            
            if counts[")"] < counts["("]:
                comb.pop()
                counts[paran] += 1
                continue
            
            util(comb)
            comb.pop()
            counts[paran] += 1