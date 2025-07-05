class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""
        j = 0
        flag = False
        for i in range(len(strs[0])):
            curr = ""
            for el in strs:
                if j > len(el) - 1:
                    flag = True
                    break
                if curr == "":
                    curr = el[j]
                else:
                    if curr != el[j]:
                        return ans
            ans += curr
            if flag:
                break
            else:
                j += 1

strs = [""]
sol = Solution()
print(sol.longestCommonPrefix(strs=strs))
