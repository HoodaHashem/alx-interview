#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is
numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


class Graph:
    """
    this class to initialize the Graph
    """

    def __init__(self, boxes):
        self.d = {}
        for i in range(len(boxes)):
            self.d[i] = boxes[i]

    def markAll(self, node):
        """to mark all the visited nodes in the graph"""

        self.d[node].append('#')
        for i in self.d[node]:
            if i == '#':
                continue
            if '#' not in self.d[i]:
                self.markAll(i)
        return self.d


def canUnlockAll(boxes):
    """
    unlock all boxes
    """
    d = Graph(boxes=boxes).markAll(0)
    for values in d.values():
        if '#' not in values:
            return False
    return True
