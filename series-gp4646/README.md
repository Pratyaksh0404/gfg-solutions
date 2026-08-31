# [N-th Term of GP](https://www.geeksforgeeks.org/problems/series-gp4646/1)

**Difficulty:** Easy

Given three integers **a**, **r**, and **n**, where **a**is the first term of a **geometric progression** (GP), **r** is the common ratio, and **n** is the position of the term you need to find. Your task is to calculate the**n-th** term of the **GP**.
Since the result can be very large, return the answer modulo 1000000007 (i.e. 10^9+ 7).

**Examples:**

```
Input: a = 2, r = 2, n = 4
Output: 16
Explanation: The GP series is 2, 4, 8, 16, 32,... in which 16 is the 4th term.
```

```
Input: a = 4, r = 3, n = 3
Output: 36
Explanation: The GP series is 4, 12, 36, 108,... in which 36 is the 3rd term.
```

**Constraints:**
- `1 ≤ a, r, n ≤ 10^6`
