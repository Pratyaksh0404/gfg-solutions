# [Finding Profession](https://www.geeksforgeeks.org/problems/finding-profession3834/1)

**Difficulty:** Medium

Consider a special family of **Engineers** and **Doctors**with following rules :

- Everybody has two children.
- First child of an Engineer is an Engineer and second child is a Doctor.
- First child of an Doctor is Doctor and second child is an Engineer.
- All generations of Doctors and Engineers start with Engineer.

The first few levels of the family tree are shown below :

Given the 1-based **level** and **pos**(position from left) of a person in above ancestor tree, return their profession as a string: either "Engineer" or "Doctor".

**Examples:**

```
Input: level = 4, pos = 2
Output: Doctor
Explanation: It is shown in the tree given in question.
```

```
Input: level = 3, pos = 4
Output: Engineer
Explanation: Already given in the tree in question.
```

**Constraints:**
- `1 ≤ level ≤ 10^9`
- `1 ≤ pos ≤ 10^9`
