import merge_sort

def main():
    import random
    array = [random.randint(1, 100) for _ in range(10)]
    print(f"unsorted array: {array}")
    sorted_array = merge_sort.merge_sort(array)
    print(f"sorted array: {sorted_array}")


if __name__ == "__main__":
    main()