from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            keylist = [0] * 26
            for char in word:
                keylist[ord(char) - ord("a")] +=1
            
            hashmap[tuple(keylist)].append(word)
        return hashmap.values()


test1 = Solution()
test1.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
test2 = Solution()
test2.groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"])