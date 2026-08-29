# [Numbers with Constraints on Digits and Digit Sum](https://www.geeksforgeeks.org/problems/special-digits--170647/1)

**Difficulty:** Hard

Given five integers **n**, **a**, **b**, **c**, and **d,**find the **total**number of best integers of length **n**.

- A good integer is an integer of length **n** such that every digit in its decimal representation is either **a** or **b**.
- A **best** integer is a good integer whose sum of digits contains at least one of the digits **c** or **d** in its decimal representation.

Since the answer can be very large, return it modulo **10^9+7**.

**Examples:**

```
Input: n = 2, a = 1, b = 2, c = 3, d = 5
Output: 2
Explanation: All 2-digit integers formed using only the digits 1 and 2 are 11, 12, 21, and 22. Their digit sums are 2, 3, 3, and 4 respectively. Since a best integer must have a digit sum containing either 3 or 5, only 12 and 21 satisfy the condition. Therefore, the answer is 2.
```

```
Input: n = 1, a = 1, b = 1, c = 2, d = 3
Output: 0
Explanation: The only 1-digit integer that can be formed using the digits 1 and 1 is 1. Its digit sum is also 1, which does not contain either c = 2 or d = 3. Therefore, there are no best integers, so the answer is 0.
```

```
Input: n = 4, a = 6, b = 7, c = 5, d = 3
Output: 4
Explanation: All 4-digit integers formed using only the digits 6 and 7 are considered good integers. Among them, the integers 6667, 6676, 6766, and 7666 have a digit sum of 25. Since the decimal representation of 25 contains C = 5, these integers are best integers. Therefore, the total number of best integers is 4.
```

**Constraints:**
1 ≤ a, b, c, d ≤ 9
1 ≤ n ≤ 10^5
