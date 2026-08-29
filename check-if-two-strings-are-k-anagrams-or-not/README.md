# [k-Anagram](https://www.geeksforgeeks.org/problems/check-if-two-strings-are-k-anagrams-or-not/1)

**Difficulty:** Medium

Given two strings **s1** and **s2** consisting of lowercase English alphabets, and an integer value **k**, return **true** if two strings are k-anagrams of each other. Otherwise, return **false**.

Two strings are called k-anagrams if****both of the below****conditions are true.

1. Both have same****number of characters.
2. Two strings can become anagram by changing****at most k characters in a string.

**Example:**

```
Input: s1 = "fodr", s2 = "gork", k = 2
Output: true
- `Explanation: We can change 'f' -> 'g' and 'd' -> 'k' in s1.`
```

```
Input: s1 = "geeks", s2 = "eggkf", k = 1
Output: false
Explanation: We can update or modify only 1 value but there is a need of modifying 2 characters i.e. 'g' and 'f' in s2.
```

```
Input: s1 = "adb", s2 = "fdab", k = 2
Output: false
Explanation: Both the strings have different numbers of characters.
```

**Constraints:**
- `1 ≤ s1.size(), s2.size() ≤ 10^5`
- `1 ≤ k ≤ 10^5`
