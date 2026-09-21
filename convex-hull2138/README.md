# [Convex Hull](https://www.geeksforgeeks.org/problems/convex-hull2138/1)

**Difficulty:** Hard

You are given a 2D array**points[][]**, where each element represents a point **(x_i , y_i)**in a 2D plane. Your task is to find all the points that form the convex hull.

A convex hull is the smallest convex polygon that encloses all the given points. It is the****minimal boundary that encloses all the points such that every line segment connecting any two points within the hull lies entirely inside or on the boundary of the polygon.

- If the given points are insufficient or do not form a valid convex polygon, return **-1**.
- You can return the points in any order, the driver code will print them in sorted order only.

**Examples:**

```
Input: points[][] = [[0, 0], [1, -4], [-1, -5], [-5, -3], [-3, -1],                   [-1, -3], [-2, -2], [-1, -1], [-2, -1], [-1, 1]]
Output: [[-5, -3], [-1, -5], [-1, 1], [0, 0], [1, -4]]Explanation: The figure below shows the points of a convex polygon. These points define the boundary of the polygon.
```

```
Input: points[][] = [[-2, 1], [4, 4], [1, -2], [1, 1], [2, 1]]
Output: [[-2, 1], [1, -2], [4, 4]]
```
**Constraints:**
- `1 <= points.size() <= 10^4`
- `-10^5 <= x_i , y_i <= 10^5`
