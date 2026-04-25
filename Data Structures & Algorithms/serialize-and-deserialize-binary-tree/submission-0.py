# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""

        def dfs(node):
            nonlocal res
            # preorder traversal
            # add value to res
            if node:
                res += str(node.val) + ","
                # traverse the other branches
                dfs(node.left)
                dfs(node.right)
            else:
                res += "N,"
        dfs(root)
        return res[0:len(res) - 1]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # convert that string into an array
        # [1,2,3,null,null,4,5]
        # split into a array
        if len(data) == 0:
            return None
        # convert the data ex: "2,4,5", "4" to array
        split = data.split(",") # ["2","4","5"]
        if split[0] == "N":
            return None
        # print(split)
        # convert the 
        root = TreeNode(int(split[0]))
        # when you encounter a N finish the subtree
        # move down the tree
        i = 1
        # when we encounter a value 
        def dfs(node):
            nonlocal i
            if i >= len(split):
                return None
            # build the left subtree of node
            if split[i] != "N":
                left = TreeNode(int(split[i]))
                i += 1
                node.left = left
                # build the subtree of left
                dfs(left)
            else:
                i += 1
            if len(split) > i and split[i] != "N":
                right = TreeNode(int(split[i]))
                i += 1
                node.right = right
                # build the subtree of left
                dfs(right)
            else:
                i += 1
        dfs(root)
        return root


                
            


