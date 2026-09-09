#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        """
        :param root: the root of the binary tree
        """
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        """
        :param: the key associated with the vertex of the binary tree
        """
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

# Test tree
root = BTvertex(1200)
tree = BinaryTree(root)
tree.root.left = BTvertex(1210)
tree.root.right = BTvertex(1240)
print(tree.root.key)
print(tree.root.right.key)


#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    # Your code goes here
    '''
    include urself if u exist as well as the number of children
    that your children have.
    recursive.
    '''
    # tree = BinaryTree(v)
    # size includes self
    v.size = 1
    if v.left != None:
        calculate_sizes(v.left)
        v.size += v.left.size
    if v.right != None:
        calculate_sizes(v.right)
        v.size += v.right.size
    return



#
# Problem 1c
#

# Input: a positive integer t, 
# ...BTvertex v, the root of a BinaryTree of size n >= 2t+1
# Output: BTvertex, descendent of v such that its size is between 
# ... t and 2t-1 (inclusive)
# Runtime: O(h) 

def FindDescendantOfSize(t, v):
    # Your code goes here 
    pass 
