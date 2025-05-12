#Part 1: AVL Tree Implementation: By Sonam Tobgay
#Part 2: Red-Black Tree Implementation: By Chesung Dorji

###Part1###

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Height of node in the tree

class AVLTree:
    def __init__(self):
        self.root = None

    # Public method to insert a value
    def insert(self, value):
        self.root = self._insert(self.root, value)

    # Internal method to insert a value starting from a given node
    def _insert(self, node, value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            # Duplicate values are not allowed in this AVL Tree
            return node

        # Update the height of the ancestor node
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

        # Get the balance factor
        balance = self._get_balance(node)

        # Perform rotations to balance the tree
        # Left Left Case
        if balance > 1 and value < node.left.value:
            return self._right_rotate(node)

        # Right Right Case
        if balance < -1 and value > node.right.value:
            return self._left_rotate(node)

        # Left Right Case
        if balance > 1 and value > node.left.value:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Left Case
        if balance < -1 and value < node.right.value:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    # Public method to delete a value
    def delete(self, value):
        self.root = self._delete(self.root, value)

    # Internal method to delete a value starting from a given node
    def _delete(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)

        elif value > node.value:
            node.right = self._delete(node.right, value)

        else:
            # Node with only one child or no child
            if not node.left:
                temp = node.right
                node = None
                return temp

            elif not node.right:
                temp = node.left
                node = None
                return temp

            # Node with two children:
            # Get the inorder successor (smallest in the right subtree)
            temp = self._get_min_value_node(node.right)

            # Copy the inorder successor's value to this node
            node.value = temp.value

            # Delete the inorder successor
            node.right = self._delete(node.right, temp.value)

        if not node:
            return node

        # Update the height of the current node
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

        # Get the balance factor
        balance = self._get_balance(node)

        # Perform rotations to balance the tree
        # Left Left Case
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)

        # Left Right Case
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Right Case
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)

        # Right Left Case
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    # Public method to search for a value
    def search(self, value):
        return self._search(self.root, value)

    # Internal method to search for a value starting from a given node
    def _search(self, node, value):
        if not node:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    # Public method to get the height of the tree
    def get_height(self):
        return self._get_height(self.root)

    # Internal method to get the height of a node
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    # Public method to check if the tree is balanced
    def is_balanced(self):
        return self._is_balanced(self.root)

    # Internal method to check if a subtree is balanced
    def _is_balanced(self, node):
        if not node:
            return True

        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)

        if abs(left_height - right_height) > 1:
            return False

        return self._is_balanced(node.left) and self._is_balanced(node.right)

    # Internal method to perform a right rotation
    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        # Return the new root
        return y

    # Internal method to perform a left rotation
    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        # Return the new root
        return y

    # Internal method to get the node with the minimum value found in a subtree
    def _get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Internal method to get the balance factor of a node
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
if __name__ == "__main__":
    avl_tree = AVLTree()
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)

    print("Is the AVL tree balanced?", avl_tree.is_balanced())  # Should return True
    print("Height of the AVL tree:", avl_tree.get_height())     # Should return 2
