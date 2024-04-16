def hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    else:
        hanoi(n - 1, source, auxiliary, destination)
        print(f"Move disk {n} from {source} to {destination}")
        hanoi(n - 1, auxiliary, destination, source)


if __name__ == "__main__":
    n = int(input())
    hanoi(n, 'A', 'C', 'B')
