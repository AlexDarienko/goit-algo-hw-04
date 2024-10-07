import timeit
import random

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Генерація випадкових масивів
def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Використання вбудованого Timsort (sorted)
def tim_sort(arr):
    return sorted(arr)

# Розміри масивів для тестування
sizes = [1000, 2000, 5000, 10000]

# Проведення тестів
for size in sizes:
    arr = generate_random_list(size)
    print(f"Тест для розміру {size}:")

    # Тест для сортування злиттям
    merge_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
    print(f"  Сортування злиттям: {merge_time:.5f} сек")

    # Тест для сортування вставками
    #if size <= 2000:  # Сортування вставками на великих масивах дуже повільне
    insertion_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
    print(f"  Сортування вставками: {insertion_time:.5f} сек")

    # Тест для Timsort (вбудоване sorted)
    timsort_time = timeit.timeit(lambda: tim_sort(arr.copy()), number=1)
    print(f"  Timsort: {timsort_time:.5f} сек")
