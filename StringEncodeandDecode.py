class Solution:

    def encode(self, strs: list[str]) -> str:
        encode = ""
        for word in strs:
            encode += str(len(word)) + word + "!$#$"
        return encode

    def decode(self, s: str) -> list[str]:
        strlist = []
        c = 0
        while(c < len(s)):
            length = int(s[c])
            word = ""
            for i in range(c+1, c+length+1):
                word += s[i]
            strlist.append(word)
            c += length+5
        return strlist


test1 = Solution()
encode1 = test1.encode(["neet","code","love","you"])
test1.decode(encode1)
test2 = Solution()
encode2 = test2.encode(["we","say",":","yes"])
test2.decode(encode2)