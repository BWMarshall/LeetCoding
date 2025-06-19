class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lookup = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }        
        if digits=="" or digits =="0" or digits == "1":
            return []


        res = ['']
        for d in digits:
            if d not in lookup:
                continue
            new_res = []
            for prev in res:
                for char in lookup[d]:
                    new_res.append(prev + char)
            res = new_res

        return res
