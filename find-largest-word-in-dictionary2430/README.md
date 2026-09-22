# [Longest Matching in Dictionary with Removals](https://www.geeksforgeeks.org/problems/find-largest-word-in-dictionary2430/1)

**Difficulty:** Medium

Given a lowercase string **s** and a dictionary **d[]** containing lowercase words, find the longest word in the dictionary that can be obtained by deleting some characters from s without changing the order of the remaining characters.

**Note**: If multiple words have the same maximum length, return the lexicographically smallest one. If no valid word exists, return an empty string.

**Examples :**

```
Input: d = ["ale", "apple", "monkey", "plea"], s = "abpcplea"Output: "apple" Explanation: After deleting "b", "c", "a" s became "apple" which is present in d.
```

```
Input: d = ["a", "b", "c"], s = "abpcplea"Output: "a"Explanation: After deleting "b", "p", "c", "p", "l", "e", "a" s became "a" which is present in d.
```
**Constraints:**
- `1 ≤ |s| ≤ 5`
- `10^51 ≤ n ≤ 10^4`
- `1 ≤ m ≤ 100`
s and all words in dictionary consist only of lowercase English letters.
