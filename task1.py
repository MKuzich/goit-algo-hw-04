import random
import timeit

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def measure_time(func, arr):
    start = timeit.default_timer()
    func(arr)
    end = timeit.default_timer()
    return end - start

random_array = [random.randint(0, 10000) for _ in range(10000)]

merge_sort_time = measure_time(merge_sort, random_array.copy())
insertion_sort_time = measure_time(insertion_sort, random_array.copy())
timsort_time = timeit.timeit(lambda: sorted(random_array), number=1)

print("Час сортування злиттям:", merge_sort_time, "секунд")
print("Час сортування вставками:", insertion_sort_time, "секунд")
print("Час Timsort:", timsort_time, "секунд")

print(f'Висновок: Сортування злиттям працює швидше за сортування вставками у {insertion_sort_time / merge_sort_time} разів, але повільніше за Timsort у {merge_sort_time / timsort_time} разів у даному конкретному випадку при тесті сортування на 10000 значень.')