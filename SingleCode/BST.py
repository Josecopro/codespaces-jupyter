class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def visualize(self, level=0, prefix="Root: "):
        print(" " * (level * 4) + prefix + str(self.value))
        if self.left:
            self.left.visualize(level + 1, prefix="L--- ")
        if self.right:
            self.right.visualize(level + 1, prefix="R--- ")


nums = [-10, -3, 0, 5, 9]


def BST(nums:list[int], Left:int = 0, Right:int = None ):
    if Right is None:
        Right = len(nums)-1

    if Left == Right:
        return BinaryTreeNode(nums[Left])

    if Left > Right:
        return None


    Mid = (Left + Right) // 2
    ola = BinaryTreeNode(nums[Mid])

    ola.left = BST(nums, Left, Mid -1)
    ola.right = BST(nums, Mid + 1, Right)

    return ola


BST(nums).visualize()

