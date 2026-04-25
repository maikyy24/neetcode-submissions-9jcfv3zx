class Codec:

    def serialize(self, root):
        #create empty list 
        tokens = []
        def dfs(node):
          # if the root is add  #         
          if node is None:
            tokens.append("#")
            return
          tokens.append(str(node.val))
          dfs(node.left)
          dfs(node.right)
        dfs(root)
        return ",".join(tokens)

    def deserialize(self, data):
      tokens = data.split(",")  # turn string back into list
      iterator = iter(tokens)   # shared, mutable position
      def build():
        token = next(iterator)
        if token == "#":
          return None
        node = TreeNode(int(token))
        node.left = build()
        node.right = build()
        return node
      return build()
