- 155. 最小栈
    ```
        设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
        push(x) -- 将元素 x 推入栈中。
        pop() -- 删除栈顶的元素。
        top() -- 获取栈顶元素。
        getMin() -- 检索栈中的最小元素。
    ```

- Python语言：使用辅助栈记录小的元素
  ```Python
  class MinStack:

      def __init__(self):
          """
          initialize your data structure here.
          """
          self.stack=[]
          self.minstack=[]
          self.length = 0

      def push(self, x: int) -> None:
          self.stack.append(x)

          if self.length == 0:
              self.minstack.append(x)
          elif x < self.minstack[-1]:
              self.minstack.append(x)
          else:
              self.minstack.append(self.minstack[-1])
          self.length += 1

      def pop(self) -> None:
          if self.length == 0:
              return False
          self.stack.pop()
          self.minstack.pop()
          self.length -=1

      def top(self) -> int:
          return self.stack[-1]

      def getMin(self) -> int:
          return self.minstack[-1]
  ```
