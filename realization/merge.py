class MergeSort:
    def __init__(self, array, time):
        self.array = array
        self.time = time

    def merge2(arr):
        if len(arr) > 1:                              
            mid = len(arr) // 2                      
            left = arr[:mid]                          
            right = arr[mid:]                         
            
            MergeSort.merge2(left)                          
            MergeSort.merge2(right) 
            
            i = j = k = 0                            
            
            while i < len(left) and j < len(right): 
                if left[i] < right[j]:               
                    arr[k] = left[i]                 
                    i+=1
                else:
                    arr[k] = right[j]
                    j+=1
                k+=1
            
            while i < len(left):
                arr[k] = left[i]
                i+=1
                k+=1
            
            while j < len(right):
                arr[k] = right[j]
                j+=1
                k+=1
        
        return arr
    
    def merge4(arr, start, first_quarter, midpoint, third_quarter, end):
        leftest_arr = arr[start:first_quarter + 1]  
        left_arr = arr[first_quarter + 1:midpoint + 1]
        right_arr = arr[midpoint + 1:third_quarter + 1]
        rightest_arr = arr[third_quarter + 1:end + 1]
        
        leftest_arr.append(float("inf"))  
        left_arr.append(float("inf"))
        right_arr.append(float("inf"))
        rightest_arr.append(float("inf"))
        
        i = j = l = m = 0
        
        for k in range(start, end + 1): 
            if leftest_arr[i] <= left_arr[j] and leftest_arr[i] <= right_arr[l] and leftest_arr[i] <= rightest_arr[m]:
                arr[k] = leftest_arr[i]
                i += 1
            elif left_arr[j] <= right_arr[l] and left_arr[j] <= rightest_arr[m]:
                arr[k] = left_arr[j]
                j += 1
            elif right_arr[l] <= rightest_arr[m]:
                arr[k] = right_arr[l]
                l += 1
            else:
                arr[k] = rightest_arr[m]
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
