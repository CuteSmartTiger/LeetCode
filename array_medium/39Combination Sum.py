# 39.Combination Sum
class Solution:
    # 递归的思路
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 去重后的列表
        candidates = list(set(candidates))
        sorted(candidates)
        self.result= []
        # 从第一个数进行判断
        start=0
        # 调用计算组合的函数
        self.backtrack(candidates, target,start,[])
        print(self.result)
        return self.result
    # 定义递归函数   candidates = [2,3,5]
    def backtrack(self,candidates,target,start,val):
        if target == 0:
            self.result.append(val[:])
            # print(self.result)
        for i in range(start,len(candidates)):
            if target>0:
                val.append(candidates[i])
                # print(val)
            else:
                break
            self.backtrack(candidates, target - candidates[i], i,val)
            val.pop()


C=Solution()
C.combinationSum(candidates = [2,3,5],target = 8)

# x=[]
# for i in range(5):
#     x.append(i)   #从右边追加
# print(x)
#
# print(x.pop())    #从右边剔除
# print(x)
# # print(x[:])