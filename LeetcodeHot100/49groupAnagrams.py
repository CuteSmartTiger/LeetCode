import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collects = collections.defaultdict(list)
        for value in strs:
            new_str = ''.join(sorted(value))
            collects[new_str].append(value)

        return list(collects.values())

s = Solution()

import unittest

class TeststgroupAnagrams(unittest.TestCase):

    def test_many_strs(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        outputs = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        results = s.groupAnagrams(strs)
        self.assertEqual(results, outputs)


if __name__ == '__main__':
    unittest.main()



