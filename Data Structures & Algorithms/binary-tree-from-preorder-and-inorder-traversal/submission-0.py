# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {val: i for i,val in enumerate(inorder)}
        self.pt = 0

        def construct_t(left,right):
            if left > right:
                return None
            val = preorder[self.pt]
            self.pt += 1

            node = TreeNode(val)
            mid = index[val]

            node.left = construct_t(left,mid-1)
            node.right = construct_t(mid+1,right)

            return node
        return construct_t(0,len(inorder)-1)