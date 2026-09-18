# [Delete Middle of Linked List](https://www.geeksforgeeks.org/problems/delete-middle-of-linked-list/1)

**Difficulty:** Easy

Given a singly linked list, delete the middle****of the linked list.

Note:

- If there are even nodes, then there would be two middle nodes, we need to delete the second****middle element.
- If the input linked list has a single node, then it should return **NULL.**

**Examples:**

```
- `Input: LinkedList: 1->2->3->4->5`
- `Output: 1->2->4->5Explanation:`
```

```
- `Input: LinkedList: 2->4->6->7->5->1`
- `Output: 2->4->6->5->1Explaination:`
```

```
- `Input: LinkedList: 7 Output: <empty linked list>Explanation: There was only one node and it was deleted.`
```

**Constraints:**
- `1 <= number of nodes <= 10^5`
- `1 <= node->data <= 10^9`
