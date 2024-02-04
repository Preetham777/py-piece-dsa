class Node:
    """
    Class Node

    arguments:
    value : Current None value           | str | None 
    left  : Current Node left pointer    | -   | None - Typically holds Node objects (left child node)
    right : Current Node right pointer   | -   | None - Typically holds Node objects (right child node)
    """
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right


    def __repr__(self):
        return(f"{self.value}")

def dressrosaDFS(node: Node) -> None:
    if node is not None:
      print(node)
      dressrosaDFS(node.left)
      dressrosaDFS(node.right)


if __name__ == "__main__" :
     # Define your root here
     # Take a look at example for the usage and output
     root = Node("A")
  
     dressrosaDFS(root)


# Example

'''
+------+
Graphs : 
+------+

                A
        B              C
    D       E     None     F


+-------------+
Node Creation :
+-------------+

# A
root = Node("A")
root.left = Node("B")
root.right = Node("C")

# B 
root.left.left = Node("D")
root.left.right = Node("E")

# C
root.right.right = Node("F")

# E
root.left.right.right = Node("F")

dressrosaDFS(root)


+------+
Output :
+------+

A
B
D
E
F
C
'''






