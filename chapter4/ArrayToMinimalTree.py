class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        if not self.left and not self.right:
            return str(self.val)
        return str(self.left) + ' , ' +  str(self.val) + ' , ' + str(self.right)

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if len(nums) == 0:
        return None
    
    mid = int(len(nums)/2) 
    
    tree = TreeNode(nums[mid])
    tree.left = sortedArrayToBST(nums[:mid])
    tree.right = sortedArrayToBST(nums[mid+1:])
    
    return tree

if __name__ == '__main__':
    print(sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]))
    print(sortedArrayToBST([-10,-3,0,5,9]))
    