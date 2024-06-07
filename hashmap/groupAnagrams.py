import collections
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collects = collections.defaultdict(list)
        for item in strs:
            sorted_str = ''.join(sorted(item))
            collects[sorted_str].append(item)
        return list(collects.values())
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for item in strs:
            sorted_str = ''.join(sorted(item))
            if sorted_str not in res:
                res[sorted_str] = [item]
            else:
                res[sorted_str].append(item)
        return res.values()


if __name__ == '__main__':
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(strs))
