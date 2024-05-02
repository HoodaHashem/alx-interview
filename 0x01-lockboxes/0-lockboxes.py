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


def unlockAll(boxes, lst):
    """unlocks all the boxes in the lst"""

    if lst == []:
        return
    lst2 = []
    for i in lst:
        try:
            if True not in boxes[i]:
                lst2.extend(boxes[i])
        except Exception as e:
            return
        boxes[i].append(True)
    unlockAll(boxes=boxes, lst=lst2)
    return boxes


def canUnlockAll(boxes):

    """
    unlock all boxes
    """

    if boxes == [] or boxes == [[]]:
        return True
    checks = unlockAll(boxes, boxes[0])
    checks[0].append(True)
    for i in range(len(checks)):
        if True in checks[i]:
            pass
        else:
            return False
    return True
