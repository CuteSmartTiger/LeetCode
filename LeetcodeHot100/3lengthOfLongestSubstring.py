class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0
        cur_length = 0
        left = 0
        n = len(s)
        visited_set = set()

        for i in range(n):
            cur_length += 1
            while s[i] in visited_set:
                visited_set.remove(s[left])
                cur_length -= 1
                left += 1
            if cur_length > max_length:
                max_length = cur_length

            visited_set.add(s[i])

        return max_length