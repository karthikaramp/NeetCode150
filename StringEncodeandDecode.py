class Solution:

    def encode(self, strs: list[str]) -> str:
        encode = ""
        for word in strs:
            encode += str(len(word))+ "!$#$" + word
        return encode

    def decode(self, s: str) -> list[str]:
        strlist = []
        c = 0
        while(c < len(s)):
            i = c
            while(s[i] != "!"):
                i += 1
            length = int(s[c:i])
            word = s[i+4: i+length+4]
            strlist.append(word)
            c = i+length+4
        return strlist


test1 = Solution()
encode1 = test1.encode(["neet","code","love","you"])
test1.decode(encode1)
test2 = Solution()
encode2 = test2.encode(["we","say",":","yes","!@#$%^&*()"])
test2.decode(encode2)