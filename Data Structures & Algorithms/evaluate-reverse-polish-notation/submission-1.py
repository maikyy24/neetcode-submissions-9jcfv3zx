class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
          if t not in {"/", "*", "+", "-"}:
            stack.append(int(t))
          else:
              a = stack.pop()
              b = stack.pop()
              if t == "+":
                stack.append( a + b)
              elif t == "-":
                stack.append( b- a) 
              elif t == "*":
                stack.append( a * b)                             
              elif t == "/":
                stack.append( int(b / a))
        return stack.pop()
    