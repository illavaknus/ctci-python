class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value, end=' ')
        in_order_traversal(node.right)

def pre_order_traversal(node):
    if node:
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=' ')

if __name__ == '__main__':
    tree = Node('A',Node('B',Node('D'),Node('E')),Node('C',Node('F'),Node('G')))
    
    print('\nIn Order Traversal: ')
    in_order_traversal(tree)
    print('\nPre Order Traversal: ')
    pre_order_traversal(tree)
    print('\nPost Order Traversal: ')
    post_order_traversal(tree)
    print('\n')