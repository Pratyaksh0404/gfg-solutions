# [Check Sum String](https://www.geeksforgeeks.org/problems/additive-sequence/1)

**Difficulty:** Medium

Given a string **s**, determine whether it represents a sum string****or not. A string is said to be a sum string if its digits can form a sequence of numbers where each number is equal to the sum of the previous two numbers.

**Note:**A valid sum string must contain at least three numbers.

**Examples:**

```
Input: n = "1235813"
Output: true
Explanation: The given string can be splited into a series of numbers  where each number is the sum of the previous two numbers: 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8, and 5 + 8 = 13. Hence, the output would be true.
```

```
Input: n = "11235815"
Output: false
Explanation: We can start with the first two digits: "11".
First number: 1, Second number: 1, Sum: 1 + 1 = 2
Now, we have "2" as the next number.
First number: 1, Second number: 2, Sum: 1 + 2 = 3
Now, we have "3" as the next number.
First number: 2, Second number: 3, Sum: 2 + 3 = 5
Now, we have "5" as the next number.
First number: 3, Second number: 5, Sum: 3 + 5 = 8
Now, we have "8" as the next number.
First number: 5, Second number: 8, Sum: 5 + 8 = 13
At this point, there is no "13" present in the remaining digits "815". Hence, the output would be false.
```

**Constraints:**
- `3 ≤ s.size() ≤ 200`
- `1 ≤ digits of string ≤ 9`
