# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path_sum = float("-inf")
        
        if root == None:
            return 0
        self.get_max_gain(root)
        return self.max_path_sum
        
    # For the current node, get the max gain from it using recursion
    def get_max_gain(self, node):
        # NULL node, max gain would be zero
        if node == None:
            return 0
        
        # Calculate the maximum gain from the left child and right child
        left_max_gain = max(self.get_max_gain(node.left), 0)
        right_max_gain = max(self.get_max_gain(node.right), 0)
        # Q: why compared with zero? negative node
        
        # Decided if we need to start a new path and update the max_path_sum
        new_path_price = node.val + left_max_gain + right_max_gain
        self.max_path_sum = max(self.max_path_sum, new_path_price)
        
        # return back to the previous phase (not include both children)
        return node.val + max(left_max_gain, right_max_gain)

    
    
 ### https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
