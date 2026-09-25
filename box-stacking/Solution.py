class Solution:
    def maxHeight(self, height: list[int], width: list[int], length: list[int]) -> int:
        boxes = []
        for h, w, l in zip(height, width, length):
            dims = sorted([h, w, l])
            boxes.extend(
                [
                    (dims[0], dims[1], dims[2]),
                    (dims[0], dims[2], dims[1]),
                    (dims[1], dims[2], dims[0]),
                ]
            )

        boxes = list(set(boxes))
        boxes.sort(key=lambda x: x[0] * x[1], reverse=True)

        n = len(boxes)
        dp = [b[2] for b in boxes]

        for i in range(1, n):
            for j in range(i):
                if boxes[i][0] < boxes[j][0] and boxes[i][1] < boxes[j][1]:
                    dp[i] = max(dp[i], dp[j] + boxes[i][2])

        return max(dp)