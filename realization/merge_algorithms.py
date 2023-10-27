from abc import ABC, abstractmethod


class MergeSort2(ABC):
    def __init__(self, array: list) -> None:
        self.array = array

    @abstractmethod
    def sort(self) -> list:
        pass

    def _merge(self, left: list, right: list) -> list:
        merged = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged.extend(left[left_index:])
        merged.extend(right[right_index:])
        return merged


class RecursiveMergeSort(MergeSort2):
    def sort(self) -> list:
        if len(self.array) <= 1:
            return self.array

        mid = len(self.array) // 2
        left_half = self.array[:mid]
        right_half = self.array[mid:]

        left_merge_sort = RecursiveMergeSort(left_half)
        right_merge_sort = RecursiveMergeSort(right_half)

        left_sorted = left_merge_sort.sort()
        right_sorted = right_merge_sort.sort()
        return self._merge(left_sorted, right_sorted)


class IterativeMergeSort(MergeSort2):
    def sort(self) -> list:
        if len(self.array) <= 1:
            return self.array

        queue = []

        for item in self.array:
            queue.append([item])

        while len(queue) > 1:
            first = queue.pop(0)
            second = queue.pop(0)
            merged = self._merge(first, second)
            queue.append(merged)
        return queue[0]
    