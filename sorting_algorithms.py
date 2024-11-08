import time

class SortingAlgorithms:

    def __init__(self):
        self.curr_time_used = 0
        self.total_time = 0

    def get_time(self):
        return self.curr_time_used
######################################################
    def bubble_sort(self, unsorted_array):
        initial_time = time.time()
        lenght = len(unsorted_array) # lenght - 1 = last index

        for i in range(lenght):
            for j in range(lenght - 1 - i):
                if unsorted_array[j] > unsorted_array[j + 1]:
                    unsorted_array[j], unsorted_array[j + 1] = unsorted_array[j + 1], unsorted_array[j]

        final_time = time.time()
        delta_time = final_time - initial_time
        self.total_time = self.curr_time_used + delta_time
        self.curr_time_used = delta_time

        return unsorted_array
###################################################
    def selection_sort(self, unsorted_array):
        initial_time = time.time()

        lenght = len(unsorted_array)

        for i in range(lenght):

            jMin = i # index minimo inicial é o primeiro
            for j in range(i + 1, lenght): # testa dps dos numeros ja arranjados
                if unsorted_array[j] < unsorted_array[jMin]:
                    jMin = j 

            if jMin != i:
                unsorted_array[i], unsorted_array[jMin] = unsorted_array[jMin], unsorted_array[i]

        final_time = time.time()
        delta_time = final_time - initial_time
        self.total_time = self.curr_time_used + delta_time
        self.curr_time_used = delta_time

        return unsorted_array
###################################################
    def insertion_sort(self, unsorted_array):
        initial_time = time.time()

        length = len(unsorted_array)

        for i in range(1, length):
            current_value = unsorted_array[i]
            j = i - 1
            while j >= 0 and unsorted_array[j] > current_value:
                unsorted_array[j + 1] = unsorted_array[j]
                j -= 1
            unsorted_array[j + 1] = current_value
 
        final_time = time.time()
        delta_time = final_time - initial_time
        self.total_time = self.curr_time_used + delta_time
        self.curr_time_used = delta_time

        return unsorted_array
###################################################

    def merge(self, left : list, right : list):
        merged = []
        left_i, right_i = 0, 0

        while left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                merged.append(left[left_i])
                left_i += 1
            else:
                merged.append(right[right_i])
                right_i += 1
        
        merged.extend(left[left_i:])
        merged.extend(right[right_i:])
        return merged
    
    def merge_sort(self, arr : list):
        initial_time = time.time()

        if len(arr):
            return arr
        
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)

        final_time = time.time()
        delta_time = final_time - initial_time
        self.total_time = self.curr_time_used + delta_time
        self.curr_time_used = delta_time

        return self.merge(left_half, right_half)
    
###########################################
    def quick_sort(self, arr : list):
        initial_time = time.time()

        if len(arr) <= 1:
            final_time = time.time()
            delta_time = final_time - initial_time
            self.total_time = self.curr_time_used + delta_time
            self.curr_time_used = delta_time

            return arr
        else:
            
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            mid = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]

            final_arr = self.quick_sort(left) + mid + self.quick_sort(right)

        final_time = time.time()
        delta_time = final_time - initial_time
        self.total_time = self.curr_time_used + delta_time
        self.curr_time_used = delta_time

        return final_arr