'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''

class Solution:
    def reverseWord(self, s, l: int, r: int) -> None:
        print(f'l:{l} r{r}')
        while (l < r):
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1

    def reverseWords(self, s: str) -> str:
        lst = list(s)
        l = 0
        r = 0
        n = len(lst)
        print(f'lst:{lst}')

        while (r <= n):
            if (r == n or lst[r] == ' '):
                self.reverseWord(lst, l, r-1)
                l = r + 1
            r += 1
           
        return ''.join(lst)


s = Solution()
str = "Let's take LeetCode contest"
print(f'Input:{str}')
res = s.reverseWords(str)
print(f'res:{res}')