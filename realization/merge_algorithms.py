from abc import ABC, abstractmethod


class MergeSort(ABC):
    def __init__(self, array):
        self.array = array

    @abstractmethod
    def sort(self):
        pass

    def _merge(self, left, right):
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


class RecursiveMergeSort(MergeSort):
    def sort(self):
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


class IterativeMergeSort(MergeSort):
    def sort(self):
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
    

"""
    # 2-way merge sort
    def mergesort2(self):
        if self.length > 1:
            print("len > 1")

            self.mergesort2(self.left)
            self.mergesort2(self.right)

            i = j = k = 0
            while i < self.length_left and j < self.length_right:
                if self.left[i] < self.right[j]: 
                    self.array[k] = self.left[i] 
                    i+=1
                else: 
                    self.array[k] = self.right[j] 
                    j+=1
                k+=1

            while i < self.length_left: 
                self.array[k] = self.left[i] 
                i+=1
                k+=1
            
            while j < self.length_right:
                self.array[k] = self.right[j]
                j+=1
                k+=1
        print(self.array)


    # 4-way merge sort
    def merge4(self, start, first_quarter, midpoint, third_quarter, end):
        leftest_arr = self.array[start:first_quarter + 1]  
        left_arr = self.array[first_quarter + 1:midpoint + 1]
        right_arr = self.array[midpoint + 1:third_quarter + 1]
        rightest_arr = self.array[third_quarter + 1:end + 1]
        
        leftest_arr.append(float("inf"))  
        left_arr.append(float("inf"))
        right_arr.append(float("inf"))
        rightest_arr.append(float("inf"))
        
        i = j = l = m = 0
        
        for k in range(start, end + 1): 
            if leftest_arr[i] <= left_arr[j] and leftest_arr[i] <= right_arr[l] and leftest_arr[i] <= rightest_arr[m]:
                self.array[k] = leftest_arr[i]
                i += 1
            elif left_arr[j] <= right_arr[l] and left_arr[j] <= rightest_arr[m]:
                self.array[k] = left_arr[j]
                j += 1
            elif right_arr[l] <= rightest_arr[m]:
                self.array[k] = right_arr[l]
                l += 1
            else:
                self.array[k] = rightest_arr[m]
                m += 1

    def mergesort4(arr, start, end):
        if end - start > 0:
            midpoint = (start + end) // 2  
            fq = (start + midpoint) // 2
            tq = (midpoint + end) // 2
            
            MergeSort.mergesort4(arr, start, fq)
            MergeSort.mergesort4(arr, fq + 1, midpoint)
            MergeSort.mergesort4(arr, midpoint + 1, tq)
            MergeSort.mergesort4(arr, tq + 1, end)
            MergeSort.merge4(arr, start, fq, midpoint, tq, end)
        
        return arr
        """
        
array = [1, 5, 3, 2, 4, 6, 7, 8, 9, 10]

recursive_sorter = RecursiveMergeSort(array)
recursive_sorted = recursive_sorter.sort()
print(recursive_sorted)

iterative_sorter = IterativeMergeSort(array)
iterative_sorted = iterative_sorter.sort()
print(iterative_sorted)