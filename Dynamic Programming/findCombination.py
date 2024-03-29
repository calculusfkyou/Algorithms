def find_combinations(n):
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path)
            return
        for i in range(start, n + 1):
            if remaining - i >= 0:
                backtrack(i, path + [i], remaining - i)

    result = []
    backtrack(1, [], n)
    return result


# Example usage:
n = int(input())
combinations = find_combinations(n)
print(combinations)
