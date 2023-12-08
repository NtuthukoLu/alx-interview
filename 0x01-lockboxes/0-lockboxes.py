#!/usr/bin/python3
"""Solves lockboxes puzzle"""


def canUnlockAll(boxes):
    """ Set to keep track of visited boxes
        and stack to perform DFS
    """
    visited = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                stack.append(key)

    return len(visited) == len(boxes)
