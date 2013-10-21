import Sort

class QuickSort(Sort.Sort):

    def sort(self, arr):
        """ Sorts array with quick sort """
        self.sortRecursive(arr, 0, len(arr) - 1)
        return arr

    def sortRecursive(self, arr, start, end):
        if (end <= start):
            return arr
        # partition using a pivot
        index = self.partition(arr, start, end)

        # sort left side of array
        if (start < index - 1):
            self.sortRecursive(arr, start, index - 1)

        # sort right side of array
        if (index < end):
            self.sortRecursive(arr, index, end)

    def partition(self, arr, start, end):
        """ paritions array based on a pivot which is found in middle of array (should work well for arrays which are mostly sorted already)"""
        pivot = arr[int((start + end) / 2)]
        left_pointer = start
        right_pointer = end
        while(left_pointer <= right_pointer):
            # move pointers closer to each other as long as items are on the correct side of pivot.
            while(arr[left_pointer] < pivot):
                left_pointer += 1
            while(arr[right_pointer] > pivot):
                right_pointer -= 1

            # swap items that are on wrong sides of pivot
            if (left_pointer <= right_pointer):
                self.swap(arr, left_pointer, right_pointer)
                left_pointer += 1
                right_pointer -= 1
        return left_pointer


    def swap(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

ms = QuickSort()
print(ms.sort([-2, 45, 0, 1, 1, -5, 3, 4, 5]))
print(ms.sort([]))
print(ms.sort([42]))
print(ms.sort(["lemon", "banana", "apple"]))
ms.benchmark()




