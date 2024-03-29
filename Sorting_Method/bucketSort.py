def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


def bucket_sort(arr):
    n = len(arr)
    max_val = max(arr)
    min_val = min(arr)
    bucket_size = 10  # Choosing arbitrary bucket size
    num_buckets = (max_val - min_val) // bucket_size + 1

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Add elements to buckets
    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[index].append(num)

    # Sort each bucket using insertion sort
    for bucket in buckets:
        insertion_sort(bucket)

    # Concatenate sorted buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        arr = list(map(int, input().split()))
        sorted_arr = bucket_sort(arr)
        print(" ".join(map(str, sorted_arr)))
