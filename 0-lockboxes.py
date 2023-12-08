#!/usr/bin/python3

def canUnlockAll(boxes):
    # Set to keep track of visited boxes
    visited = set()
    # Stack to perform DFS
    stack = [0]  # Start with the first box (index 0)

    while stack:
        current_box = stack.pop()
        visited.add(current_box)

        # Add new keys to the stack
        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                stack.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)

