class Solution:
    def countSeniors(self, details: List[str]) -> int:
        if not details: return 0
        res = 0
        for d in details:
            if int(d[11:13]) > 60:
                res += 1
        
        return res
        