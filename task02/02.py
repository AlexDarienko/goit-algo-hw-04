import heapq

def merge_k_lists(lists):
    # Ініціалізуємо порожній список результатів та мін-кучу
    result = []
    min_heap = []
    
    # Додаємо перші елементи всіх списків до кучи
    for i, lst in enumerate(lists):
        if lst:  # Перевіряємо, чи список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    # Зливаємо списки
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        
        # Якщо є наступний елемент в поточному списку, додаємо його до кучи
        if element_idx + 1 < len(lists[list_idx]):
            heapq.heappush(min_heap, (lists[list_idx][element_idx + 1], list_idx, element_idx + 1))
    
    return result

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
