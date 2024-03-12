
def tree_size(root):
    p = root
    if p is None:
        return 0
    else:
        return 1 + tree_size(p.left) + tree_size(p.right)
    
def tree_height(root):
    p = root
    if p is None:
        return 0
    else:
        return 1 + max(tree_height(p.left), tree_height(p.right))
    
def tree_leaves(root):
    p = root
    if p is None:
        return 0
    elif p.left is None and p.right is None:
        return 1
    else:
        return tree_leaves(p.left) + tree_leaves(p.right)
    
def tree_for_level(root, level):
    pass



