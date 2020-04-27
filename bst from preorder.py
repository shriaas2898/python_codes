# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''Function to create binary search tree from its preorder of elements
    '''
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        for i in preorder[1:]:
            temp = root
            added = False
            while(not added):
                if(i<temp.val):
                    if(temp.left == None):
                        newNode = TreeNode(i)
                        temp.left = newNode
                        added = True
                        break
                    temp = temp.left
                    continue
                    
                else:
                    if(temp.right == None):
                        newNode = TreeNode(i)
                        temp.right = newNode
                        added = True
                        break
                    temp = temp.right
                    continue
        
        return root            
                    
                
    
        
