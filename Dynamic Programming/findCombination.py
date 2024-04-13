# 找出所有n的組合
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


# 找字串的所有排列組合
# def permutation(str1, i, n):
#     if i == n:
#         print("".join(str1))
#     else:
#         for j in range(i, n):
#             str1[i], str1[j] = str1[j], str1[i]
#             permutation(str1, i + 1, n)
#             str1[i], str1[j] = str1[j], str1[i]
#
#
# if __name__ == "__main__":
#     str1 = list(input())
#     permutation(str1, 0, len(str1))
