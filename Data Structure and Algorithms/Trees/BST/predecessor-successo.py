from BST import BinarySearchTree,inorder,insert 

def pre_succ(root,key):
    if root is None:
        return None

    if root.data == key:
        if root.right is not None:
            tmp  = root.right
            while tmp.left:
                tmp = tmp.left
            
            pre_succ.succ = tmp 

        if root.left is not None:
            tmp = root.left
            while tmp.right:
                tmp = tmp.right
            
            pre_succ.pre = tmp 
                           
        return

    if root.data < key:
        pre_succ.pre = root
        pre_succ(root.right,key)
    elif root.data > key:
        pre_succ.succ = root
        pre_succ(root.left,key)
    
    



def isBST(root):
    if root:
        return True

    left = isBST(root.left)
    if not left:
        return False

    if isBST.prev is not None and root.data <= prev.data:
        return False

    isBST.prev = root 

    return isBST(root.right)



if __name__=='__main__':
    myTree = BinarySearchTree(6)
    insert(myTree,7)
    insert(myTree,5)
    insert(myTree,13)
    insert(myTree,3)
    insert(myTree,9)
    insert(myTree,12)    
    insert(myTree,1)
    insert(myTree,4)
    inorder(myTree)
    pre_succ.pre = None
    pre_succ.succ= None    
    searchKey = 8
    #pre_succ(myTree,searchKey)

    print("")
    #print(pre_succ.pre.data,'..',searchKey,'..',pre_succ.succ.data)
    isBST.prev = None
    print(isBST(myTree))