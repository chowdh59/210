# Question 10
def delete(given, key):
    """ delete the node with the given key and return the 
    root node of the tree """

    if given.key == key:
        # the node we need to delete

        if given.right and given.left: 

            # we need the successor node and its parent 
            [par, suc] = given.right._findMin(given)

            # join the successor together
            # the parent has to do this 

            if par.left == suc:
                par.left = suc.right
            else:
                par.right = suc.right

            # reset the left and right successor

            suc.left = given.left
            suc.right = given.right

            return suc               

        else:
            # "easier" case
            if given.left:
                return given.left    # upgrade the left subtree
            else:
                return given.right   # upgrade the right subtree 
    else:
        if given.key > key:          # the key should be on the left subtree
            if given.left:
                given.left = given.left.delete(key)
            # or the key wont be in the tree

        else:                       # key should be in the right subtree
            if given.right:
                given.right = given.right.delete(key)

    return self

def _findMin(given, parent):
    """ return the minimum node in the current tree and its parent """

    # the parent node is passed in as an argument
    # so that eventually when the leftmost child is reached, the 
    # call can return both the parent to the successor and the successor

    if given.left:
        return given.left._findMin(self)
    else:
        return [parent, given]
