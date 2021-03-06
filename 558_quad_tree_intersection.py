# easy
"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val == True else quadTree2
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val == True else quadTree1
        tl = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        tr = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bl = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        br = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        if tl.val == tr.val and tl.val == bl.val and tl.val == br.val and tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf:
            return Node(tl.val, True, None, None, None, None)
        else:
            return Node(False, False, tl, tr, bl, br)
