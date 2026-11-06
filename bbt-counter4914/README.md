# [Balanced Binary Tree Counter](https://www.geeksforgeeks.org/problems/bbt-counter4914/1)

**Difficulty:** Easy

Given a height **h**, find the maximum number of distinct balanced binary trees of height exactly h.

A binary tree is balanced if, for every node, the heights of its left and right subtrees differ by at most 1. A tree with a single node has height 1. An empty tree has height 0.

**Note:** Since the answer can be very large, return it modulo 10^9 + 7.

**Examples:**

```
Input: h = 1Output: 1Explanation: Only one tree of height 1 exists i.e. a single node.
```

```
Input: h = 2
Output: 3 
Explanation: 3 distinct balanced trees of height 2 exist.
```

```
Input: h = 3
Output: 15
Explanation: 15 distinct balanced trees of height 3 exist.
```
