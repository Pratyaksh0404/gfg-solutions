class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        n = len(s)
        if pos <= n:
            return s[pos - 1]

        ll = [n]
        steps = []
        i = 1
        while ll[-1] < pos:
            prev = ll[-1]
            ll.append(2 * prev + i)
            steps.append(i)
            i += 1

        for idx in range(len(steps) - 1, -1, -1):
            prev = ll[idx]
            dlc = steps[idx]
            if pos <= prev:
                continue
            elif pos <= prev + dlc:
                return "$"
            else:
                offset = pos - prev - dlc
                pos = prev - offset + 1

        return s[pos - 1]