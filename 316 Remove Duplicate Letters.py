class LC316:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        count = [0] * 26
        flag = [False] * 26
        for l in s:
            count[ord(l) - ord('a')] += 1
        ret = ""
        for l in s:
            count[ord(l) - ord('a')] -= 1
            if flag[ord(l) - ord('a')]:
                continue
            while len(ret) > 0 and ret[-1] > l and count[ord(ret[-1]) - ord('a')] > 0:
                flag[ord(ret[-1]) - ord('a')] = False
                ret = ret[:-1]
            ret += l
            flag[ord(l) - ord('a')] = True
        return ret
s = "cbacdcbc"
a = LC316().removeDuplicateLetters(s)
print(a)