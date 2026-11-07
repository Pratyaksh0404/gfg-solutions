class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        reserved = set(arr)
        counts = {}
        result = []

        for name in arr:
            if name not in counts:
                counts[name] = 1
                result.append(name)
            else:
                k = counts[name]
                while f"{name}{k}" in reserved:
                    k += 1
                new_name = f"{name}{k}"
                reserved.add(new_name)
                counts[name] = k + 1
                result.append(new_name)

        return result