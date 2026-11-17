# [Repeated Pattern Check](https://www.geeksforgeeks.org/problems/the-pattern-matcher/1)

**Difficulty:** Easy

Given a string **s** made of two characters of **'x'**and **'y'**.  The task is to verify whether **s** is made by concatenating substrings that follow the pattern **x^ny^n**  (equal number of y'*s* follow equal number of x'*s)*.

**Examples:**

```
Input: s = "xxyyxy" Output: trueExplanation: The string can be split into "xxyy" + "xy". Both substrings contain an equal number of consecutive 'x' and 'y' characters.
```

```
Input: s = "xyx"Output: falseExplanation: The last 'x' cannot form a valid substring because it is not followed by a matching 'y'.
```
