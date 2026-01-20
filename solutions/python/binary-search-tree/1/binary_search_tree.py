class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.sorted_data_list = []
        for index, number in enumerate(tree_data):
            if index == 0:
                self.node = TreeNode(number)
            else:
                inserted = False
                current_node = self.node
                while inserted == False:
                    if number <= current_node.data:
                        if current_node.left == None:
                            current_node.left = TreeNode(number)
                            inserted = True
                        else:
                            current_node = current_node.left
                    else:
                        if current_node.right == None:
                            current_node.right = TreeNode(number)
                            inserted = True
                        else:
                            current_node = current_node.right

    def data(self):
        return self.node

    def sorting(self, node):
        if node.left != None:
            self.sorting(node.left)

        self.sorted_data_list.append(node.data)

        if node.right != None:
            self.sorting(node.right)

    def sorted_data(self):
        self.sorting(self.node)
        return self.sorted_data_list
            
