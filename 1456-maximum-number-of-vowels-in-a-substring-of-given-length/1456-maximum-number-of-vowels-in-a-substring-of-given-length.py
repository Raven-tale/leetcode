class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans, vowels = 0, list('aeiou')
        for i in s[0:k]:
            ans += (i in vowels)
        cnt = ans
        for j in range(1, len(s) - k + 1):
            cnt += - (s[j - 1] in vowels) + (s[j + k - 1] in vowels)
            if cnt > ans:
                ans = cnt
        return ans