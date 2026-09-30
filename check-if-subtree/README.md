# [Check Subtree](https://www.geeksforgeeks.org/problems/check-if-subtree/1)

**Difficulty:** Medium

Given the roots of two binary trees, **root1** and **root2**, determine whether the tree rooted at root2 is a subtree of the tree rooted at root1.

Return true if there exists a node in the tree rooted at root1 such that the subtree rooted at that node is identical to the tree rooted at root2. Otherwise, return false.

**Note:**Two binary trees are considered identical if they have the same structure and the same node values.

**Examples:**

```
Input: root1 = [1, 2, 3, N, N, 4], root2 = [3, 4]             Output: true 
Explanation: In the tree rooted at root1, the subtree starting at node 3 is identical to the tree rooted at root2 (same structure and node values). Hence, root2 is a subtree of root1, so the output is true.
```

```
Input: root1 = [26, 10, N, 20, 30, 40, 60], root2 = [26, 10, N, 20, 30, 40, 60]                        
Output: true 
Explanation: Both root1 and root2 represent identical trees. So, root2 is a subtree of root1, and the output is true.
```
