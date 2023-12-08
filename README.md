# PROJECT: 0X01. Lockboxes
## AUTHOR: Ntuthuko Zimu
## TASK:

### canUnlockAll Function

### Description
The `canUnlockAll` function checks whether it is possible to unlock all the boxes in a given set of locked boxes. Each box is numbered sequentially from 0 to n - 1, and each box may contain keys to other boxes. The goal is to determine if, starting from the first box (which is initially unlocked), all boxes can eventually be opened.

### Function Signature
```python
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    - boxes (List[List[int]]): A list of lists where each list represents a box and contains positive integers as keys.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """


