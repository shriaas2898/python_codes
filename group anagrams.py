#File contains solution for leetcode problem: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/
'''
Function groups the anagrams present in list strs
togather and returns list of groups of anagrams
'''
def groupAnagrams(strs: List[str]) -> List[List[str]]:
        ngrams = {}
        for i in strs:
            key = ''.join(sorted(i))
            if(key in ngrams.keys()):
                 ngrams[key].append(i)
            else:
                 ngrams[key] = [i]
        return(ngrams.values())
