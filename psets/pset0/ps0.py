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
    '''
    include urself if u exist as well as the number of children
    that your children have.
    recursive.
    '''
    # base case
    if v is None:
        return 0
    # size includes self and child sizes
    v.size = 1 + calculate_sizes(v.left) + calculate_sizes(v.right)
    return v.size


#
# Problem 1c
#

# Input: a positive integer t, 
# ...BTvertex v, the root of a BinaryTree of size n >= 2t+1
# Output: BTvertex, descendent of v such that its size is between 
# ... t and 2t-1 (inclusive)
# Runtime: O(h) 

def FindDescendantOfSize(t, v):
    '''
    t is a POS INT, v is a "SIZE AUGMENTED" TREE st v.size >= 2t + 1.
    Find subtree with root w wherein t <= w.size <= 2t - 1.
    Should use calculate_sizes methinks. OOHHHH already size augmented
    '''
    # removed base cases (v is none and v.size is in range because they never hit given the
    # inputs since is always at least 2t + 1)

    # Check child size is over or perfectly already in range because
        # sum of child sizes is at least 2t so one child must be at least t
    if v.left is not None:
        # just out of range
        if (v.left.size >= 2*t):
            return FindDescendantOfSize(t, v.left)
        # if less than t ignore and go to right child
        elif (v.left.size >= t):
            return v.left
    
    if v.right is not None:
        # just out of range
        if (v.right.size >= 2*t):
            return FindDescendantOfSize(t, v.right)
        elif (v.right.size >= t):
            return v.right