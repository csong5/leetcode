# LC358: Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.
# All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".
#
# Example 1:
# Input: s = "aabbcc", k = 3
# Output: "abcabc"
# Explanation: The same letters are at least distance 3 from each other.
# Example 2:
# Input: s = "aaabc", k = 3
# Output: ""
# Explanation: It is not possible to rearrange the string.
# Example 3:
# Input: s = "aaadbbcc", k = 2
# Output: "abacabcd"
# Explanation: The same letters are at least distance 2 from each other.

class LC358:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0 or len(s) < k:
            return s
        dic = dict()
        for letter in s:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        pq = queue.PriorityQueue()
        for char, count in dic.items():
            pq.put((-count, char))
            # Note pq sorts based on the 1st element
            # can also use heapq. The difference is that pq ensures thread safety.
        ret = ""
        while not pq.empty():
            if pq.qsize() < k and -pq.queue[0][0] > 1:  # pq.queue[] => tuple(str, int)
                return ""
            n = min(pq.qsize(), k)
            temp = set()
            for _ in range(n):
                ret += pq.queue[0][1]
                temp.add(pq.get())
            for pair in temp:
                if -pair[0] > 1:
                    pq.put((pair[0]+1, pair[1]))
        return ret
s = "aaabbccd"
a = LC358().rearrangeString(s, 2)
print(a)