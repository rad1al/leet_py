# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """ 
        if t1 == None and t2 == None: # if both t1 and t2 nodes don't exist, return None
            return None
        t = TreeNode((t1.val if t1 != None else 0) + (t2.val if t2 != None else 0)) # if nodes exist, add the numbers, else add 0.
        t.left = self.mergeTrees(t1 and t1.left, t2 and t2.left) # make sure parents exists before adding. None and _ = None
        t.right = self.mergeTrees(t1 and t1.right, t2 and t2.right) # make sure parents exist before adding
        return t